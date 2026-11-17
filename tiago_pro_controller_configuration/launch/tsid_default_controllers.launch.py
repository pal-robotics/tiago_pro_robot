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

from dataclasses import dataclass
import os

from ament_index_python.packages import get_package_share_directory
from controller_manager.launch_utils import generate_load_controller_launch_description
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import GroupAction, OpaqueFunction
from launch.conditions import LaunchConfigurationNotEquals
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.param_utils import merge_param_files, parse_parametric_yaml
from launch_pal.robot_arguments import CommonArgs
from tiago_pro_description.launch_arguments import TiagoProArgs


# Explicit list of all spawnable controllers for validation and documentation
AVAILABLE_CONTROLLERS = [
    'torso_joint_space_controller',
    'torso_joint_space_vel_controller',
    'arm_right_cartesian_vel_controller_ee_frame',
    'arm_right_cartesian_vel_controller_robot_frame',
    'arm_right_joint_space_controller_vel',
    'arm_right_joint_space_controller',
    'arm_right_cartesian_space_controller_ee_frame',
    'arm_right_cartesian_space_controller_robot_frame',
    'arm_left_cartesian_vel_controller_ee_frame',
    'arm_left_cartesian_vel_controller_robot_frame',
    'arm_left_joint_space_controller_vel',
    'arm_left_joint_space_controller',
    'arm_left_cartesian_space_controller_ee_frame',
    'arm_left_cartesian_space_controller_robot_frame',
]


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    namespace: DeclareLaunchArgument = CommonArgs.namespace
    use_grasping_frame: DeclareLaunchArgument = DeclareLaunchArgument(
        name='use_grasping_frame',
        default_value='True',
        choices=['True', 'False'],
        description='If true the cartesian controller is going to move the grasping frame.',
    )

    controllers_to_spawn: DeclareLaunchArgument = DeclareLaunchArgument(
        'controllers_to_spawn',
        default_value='',
        description=(
            'Comma-separated list of controllers to launch. '
            'If empty, all default controllers are launched. '
            f"Valid options are: {', '.join(AVAILABLE_CONTROLLERS)}"
        )
    )


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    # Validate user input before trying to launch anything
    validation_step = OpaqueFunction(function=validate_controllers)
    launch_description.add_action(validation_step)

    # Setup the controllers
    right_arm_controller = OpaqueFunction(
        function=setup_arm_controllers,
        kwargs={'arm_side': 'right'},
        condition=LaunchConfigurationNotEquals('arm_type_right', 'no-arm'),
    )
    launch_description.add_action(right_arm_controller)

    left_arm_controller = OpaqueFunction(
        function=setup_arm_controllers,
        kwargs={'arm_side': 'left'},
        condition=LaunchConfigurationNotEquals('arm_type_left', 'no-arm'),
    )
    launch_description.add_action(left_arm_controller)

    torso_controller = OpaqueFunction(function=setup_torso_controllers)
    launch_description.add_action(torso_controller)

    return


def validate_controllers(context, *args, **kwargs):
    target_controllers_str = read_launch_argument('controllers_to_spawn', context)

    # If empty, spawn every controller
    if not target_controllers_str:
        return []

    target_controllers = [c.strip() for c in target_controllers_str.split(',') if c.strip()]

    # Find any controllers provided by the user that aren't in the allowed list
    invalid_controllers = [c for c in target_controllers if c not in AVAILABLE_CONTROLLERS]

    if invalid_controllers:
        raise ValueError(
            "\n\n[ERROR] Invalid controller name(s) provided in 'controllers_to_spawn': "
            f'{invalid_controllers}.\n'
            f'Please ensure you spelled them correctly.\n'
            f'Valid options are:\n- ' + '\n- '.join(AVAILABLE_CONTROLLERS) + '\n'
        )

    return []


def setup_torso_controllers(context, *args, **kwargs):
    target_controllers_str = read_launch_argument('controllers_to_spawn', context)
    target_controllers = [c.strip() for c in target_controllers_str.split(',') if c.strip()]

    available_controllers = [
        'torso_joint_space_controller',
        'torso_joint_space_vel_controller'
    ]

    controllers_to_start = []

    for ctrl in available_controllers:
        if not target_controllers or ctrl in target_controllers:
            controllers_to_start.append(
                setup_torso_controller(context, ctrl, load_gains_separately=True)
            )

    return controllers_to_start


def setup_torso_controller(
        context,
        controller_name,
        load_gains_separately=False):
    param_file = os.path.join(
        get_package_share_directory('tiago_pro_controller_configuration'),
        'config',
        'tsid',
        f'{controller_name}.yaml',
    )
    parsed_yaml = parse_parametric_yaml(
        source_files=[param_file], param_rewrites={})

    use_sim_time = read_launch_argument('use_sim_time', context)
    if load_gains_separately:
        sim_postfix = '_sim' if use_sim_time == 'True' else ''

        gains_file = os.path.join(
            get_package_share_directory('tiago_pro_controller_configuration'),
            'config',
            'tsid',
            'gains',
            f'{controller_name}{sim_postfix}.yaml',
        )

        parsed_gains = parse_parametric_yaml(
            source_files=[gains_file], param_rewrites={}
        )

        parsed_yaml = merge_param_files([parsed_yaml, parsed_gains])

    launch_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name=controller_name,
                controller_params_file=parsed_yaml,
                extra_spawner_args=['--inactive'],
            )
        ],
        forwarding=False,
    )

    return launch_controller


def setup_arm_controllers(context, arm_side, *args, **kwargs):
    target_controllers_str = read_launch_argument('controllers_to_spawn', context)
    target_controllers = [c.strip() for c in target_controllers_str.split(',') if c.strip()]

    available_base_controllers = [
        'cartesian_vel_controller_ee_frame',
        'cartesian_vel_controller_robot_frame',
        'joint_space_controller_vel',
        'joint_space_controller',
        'cartesian_space_controller_ee_frame',
        'cartesian_space_controller_robot_frame',
    ]

    controllers_to_start = []

    for base_ctrl in available_base_controllers:
        full_ctrl_name = f'arm_{arm_side}_{base_ctrl}'

        if not target_controllers or full_ctrl_name in target_controllers:
            controllers_to_start.append(
                setup_arm_side_controller(context, base_ctrl, arm_side, load_gains_separately=True)
            )

    return controllers_to_start


def setup_arm_side_controller(
    context, controller_name, arm_side='right', load_gains_separately=False
):

    arm_prefix = f'arm_{arm_side}'
    side_controller_name = f'{arm_prefix}_{controller_name}'

    # Check if the end effector frame needs to be the grasping one
    use_grasping_frame = read_launch_argument('use_grasping_frame', context)

    # Creating the end effector frame name with side
    if use_grasping_frame == 'False':
        ee_suffix = '7_link'
        ee_prefix = 'arm'
    elif use_grasping_frame == 'True':
        ee_suffix = 'grasping_link'
        ee_prefix = 'gripper'

    remappings = {'ARM_SIDE_PREFIX': arm_prefix,
                  'SIDE': arm_side,
                  'EE_PREFIX': ee_prefix,
                  'EE_SUFFIX': ee_suffix
                  }

    param_file = os.path.join(
        get_package_share_directory('tiago_pro_controller_configuration'),
        'config',
        'tsid',
        f'{controller_name}.yaml',
    )

    parsed_yaml = parse_parametric_yaml(
        source_files=[param_file], param_rewrites=remappings
    )

    use_sim_time = read_launch_argument('use_sim_time', context)
    if load_gains_separately:
        sim_postfix = '_sim' if use_sim_time == 'True' else ''

        gains_file = os.path.join(
            get_package_share_directory('tiago_pro_controller_configuration'),
            'config',
            'tsid',
            'gains',
            f'{controller_name}{sim_postfix}.yaml',
        )

        parsed_gains = parse_parametric_yaml(
            source_files=[gains_file], param_rewrites=remappings
        )

        parsed_yaml = merge_param_files([parsed_yaml, parsed_gains])

    launch_controller = GroupAction(
        [
            generate_load_controller_launch_description(
                controller_name=side_controller_name,
                controller_params_file=parsed_yaml,
                extra_spawner_args=['--inactive'],
            )
        ],
        forwarding=False,
    )

    return launch_controller


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
