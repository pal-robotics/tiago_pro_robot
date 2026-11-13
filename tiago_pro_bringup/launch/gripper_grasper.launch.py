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

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description
from tiago_pro_description.launch_arguments import TiagoProArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoProArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoProArgs.end_effector_left


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    # Add controller of left gripper
    launch_description.add_action(OpaqueFunction(
        function=set_side_gripper, args=['left'],
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration('end_effector_left'), "' == 'pal-pro-gripper' and '",
                 LaunchConfiguration('arm_type_left'), "' != 'no-arm'"]
            )
        )))

    # Add controller of right gripper
    launch_description.add_action(OpaqueFunction(
        function=set_side_gripper, args=['right'],
        condition=IfCondition(
            PythonExpression(
                ["'", LaunchConfiguration('end_effector_right'), "' == 'pal-pro-gripper' and '",
                 LaunchConfiguration('arm_type_right'), "' != 'no-arm'"]
            )
        )))
    return


def set_side_gripper(context, side='', *args, **kwargs):

    gripper_wrapper = include_scoped_launch_py_description(
        pkg_name='pal_pro_gripper_wrapper',
        paths=['launch', 'pal_pro_gripper_wrapper.launch.py'],
        launch_arguments={'side': side}
        )

    return [gripper_wrapper]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
