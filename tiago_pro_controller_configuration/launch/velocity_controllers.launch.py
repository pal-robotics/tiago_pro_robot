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
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.param_utils import parse_parametric_yaml
from launch_pal.robot_arguments import CommonArgs
from tiago_pro_description.launch_arguments import TiagoProArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):

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

    return


def setup_arm_controllers(context, arm_side, *args, **kwargs):

    forward_controller_vel = setup_arm_side_controller(
        context, 'forward_controller_vel', arm_side,
    )

    return [
        forward_controller_vel,
    ]


def setup_arm_side_controller(
    context, controller_name, arm_side='right',
):

    arm_prefix = f'arm_{arm_side}'

    side_controller_name = f'{arm_prefix}_{controller_name}'
    remappings = {'ARM_SIDE_PREFIX': arm_prefix}

    param_file = os.path.join(
        get_package_share_directory('tiago_pro_controller_configuration'),
        'config',
        f'{controller_name}.yaml',
    )

    parsed_yaml = parse_parametric_yaml(
        source_files=[param_file], param_rewrites=remappings
    )

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
