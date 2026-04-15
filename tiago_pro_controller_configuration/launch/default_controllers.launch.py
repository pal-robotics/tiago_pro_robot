# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import List
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction
from launch.conditions import LaunchConfigurationNotEquals, IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from tiago_pro_description.launch_arguments import TiagoProArgs

from dataclasses import dataclass


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    base_type: DeclareLaunchArgument = TiagoProArgs.base_type
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoProArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoProArgs.end_effector_left
    ft_sensor_right: DeclareLaunchArgument = TiagoProArgs.ft_sensor_right
    ft_sensor_left: DeclareLaunchArgument = TiagoProArgs.ft_sensor_left
    wrist_model_right: DeclareLaunchArgument = TiagoProArgs.wrist_model_right
    wrist_model_left: DeclareLaunchArgument = TiagoProArgs.wrist_model_left
    torque_estimation: DeclareLaunchArgument = TiagoProArgs.torque_estimation
    has_teleop_arms: DeclareLaunchArgument = TiagoProArgs.has_teleop_arms

    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_share_folder = get_package_share_directory(
        'tiago_pro_controller_configuration')

    # Mobile base controller
    launch_description.add_action(
        OpaqueFunction(function=launch_mobile_base_controller))

    # Joint state broadcaster
    joint_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_state_broadcaster.yaml'))
         ],
        forwarding=False)
    launch_description.add_action(joint_state_broadcaster)

    joint_torque_state_broadcaster = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='joint_torque_state_broadcaster',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'joint_torque_state_broadcaster.yaml'))
         ],
        forwarding=False,
        condition=IfCondition(
            PythonExpression([
                "(", LaunchConfiguration("torque_estimation"), ") and (('",
                LaunchConfiguration(
                    "wrist_model_right"), "' != 'short-wrist') or ('",
                LaunchConfiguration("wrist_model_left"), "' != 'short-wrist'))"
            ])
        )
    )
    launch_description.add_action(joint_torque_state_broadcaster)

    # Torso controller
    torso_controller = GroupAction(
        [generate_load_controller_launch_description(
            controller_name='torso_controller',
            controller_params_file=os.path.join(
                pkg_share_folder,
                'config', 'torso_controller.yaml'))
         ],
        forwarding=False)
    launch_description.add_action(torso_controller)

    # Head controller
    head_controller = include_scoped_launch_py_description(
        pkg_name="tiago_pro_head_controller_configuration",
        paths=["launch", "head_controller.launch.py"])
    launch_description.add_action(head_controller)

    # Add controller of right arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['right'],
        condition=LaunchConfigurationNotEquals('arm_type_right', 'no-arm')))

    # Add controller of left arm, end-effector and ft-sensor
    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['left'],
        condition=LaunchConfigurationNotEquals('arm_type_left', 'no-arm')))

    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['teleop_right'],
        condition=IfCondition(LaunchConfiguration("has_teleop_arms"))))

    launch_description.add_action(OpaqueFunction(
        function=configure_side_controllers, args=['teleop_left'],
        condition=IfCondition(LaunchConfiguration("has_teleop_arms"))))

    return


def configure_side_controllers(context, end_effector_side='right', *args, **kwargs):
    is_teleop = end_effector_side.startswith('teleop')

    if is_teleop:
        wrist_model = read_launch_argument(
            f'wrist_model_{end_effector_side.replace("teleop_", "")}', context)
        root_link_str = "pilot_station_base_link"
    else:
        wrist_model = read_launch_argument(
            f'wrist_model_{end_effector_side}', context)
        root_link_str = "torso_lift_link"

    end_effector_arg_name = concatenate_strings(
        strings=['end_effector', end_effector_side.replace('teleop_', '')],
        delimiter='_',
        skip_empty=True)

    ft_sensor_arg_name = concatenate_strings(
        strings=['ft_sensor', end_effector_side],
        delimiter='_',
        skip_empty=True)

    arm_controller = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'arm_controller.launch.py'],
        launch_arguments={
            "side": end_effector_side,
            "wrist_model": wrist_model,
        })

    sea_state_broadcaster_controller = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'sea_state_broadcaster_controller.launch.py'],
        launch_arguments={"side": end_effector_side},
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration('use_sim_time'), "' == 'False' and '",
                 LaunchConfiguration(
                     'torque_estimation'), "' == 'True' and not ('",
                 wrist_model, "' == 'short-wrist')"]
            )
        ))

    gravity_compensation_controller_effort = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'gravity_compensation_controller.launch.py'],
        launch_arguments={"side": end_effector_side,
                          "root_link": root_link_str,
                          "wrist_model": wrist_model},
        condition=UnlessCondition(LaunchConfiguration("is_public_sim")))

    gravity_compensation_controller_torque = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'gravity_compensation_controller.launch.py'],
        launch_arguments={"side": end_effector_side,
                          "mode": "torque",
                          "root_link": root_link_str},
        condition=IfCondition(
            PythonExpression([
                "(",
                LaunchConfiguration("torque_estimation"),
                ") and not ((",
                LaunchConfiguration("is_public_sim"),
                ") or (",
                "'", wrist_model, "' == 'short-wrist'",
                "))"
            ])
        ))

    use_sim_time = read_launch_argument("use_sim_time", context)

    inertia_shaping_controllers = include_scoped_launch_py_description(
        pkg_name='pal_sea_arm_controller_configuration',
        paths=['launch', 'inertia_shaping_controllers.launch.py'],
        launch_arguments={"side": end_effector_side},
        condition=IfCondition(
            PythonExpression([
                "(", LaunchConfiguration("torque_estimation"), ") and not ('",
                wrist_model, "' == 'short-wrist')"])
        ))

    end_effector = read_launch_argument(end_effector_arg_name, context)
    end_effector_underscore = end_effector.replace('-', '_')

    ee_pkg_name = f'{end_effector_underscore}_controller_configuration'
    ee_launch_file = f'{end_effector_underscore}_controller.launch.py'

    if end_effector == 'allegro-hand' and use_sim_time == 'False':
        ee_launch_file = 'allegro_hand_controller_libhand.launch.py'

    end_effector_controller = include_scoped_launch_py_description(
        pkg_name=ee_pkg_name,
        paths=['launch', ee_launch_file],
        launch_arguments={"side": end_effector_side},
        condition=LaunchConfigurationNotEquals(
            end_effector_arg_name, 'no-end-effector')
    )

    # Setup ft-sensor controller
    ft_sensor = read_launch_argument(ft_sensor_arg_name, context)
    ft_pkg_name = 'pal_sea_arm_controller_configuration'
    ft_launch_file = 'ft_sensor_controller.launch.py'

    ft_sensor_controller = include_scoped_launch_py_description(
        pkg_name=ft_pkg_name,
        paths=['launch', ft_launch_file],
        launch_arguments={"side": end_effector_side,
                          "ft_sensor": ft_sensor},
        condition=LaunchConfigurationNotEquals(
            ft_sensor_arg_name, 'no-ft-sensor')

    )

    return [arm_controller, sea_state_broadcaster_controller,
            gravity_compensation_controller_effort,
            gravity_compensation_controller_torque,
            inertia_shaping_controllers,
            end_effector_controller, ft_sensor_controller]


def concatenate_strings(strings: List[str], delimiter: str = '', skip_empty: bool = False):

    concatenated_string = ''

    if skip_empty:
        concatenated_string = delimiter.join(filter(None, strings))
    else:
        concatenated_string = delimiter.join(strings)

    return concatenated_string


def launch_mobile_base_controller(context, *args, **kwargs):

    base_type = read_launch_argument("base_type", context)
    use_sim_time = read_launch_argument("use_sim_time", context)
    is_public_sim = read_launch_argument("is_public_sim", context)

    base_controller_package = base_type + "_controller_configuration"

    mobile_base_controller = include_scoped_launch_py_description(
        pkg_name=base_controller_package,
        paths=["launch", "mobile_base_controller.launch.py"],
        launch_arguments={
            "use_sim_time": use_sim_time,
            "is_public_sim": is_public_sim,
        }
    )

    return [mobile_base_controller]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
