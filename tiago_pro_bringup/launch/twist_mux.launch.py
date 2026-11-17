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
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.robot_arguments import CommonArgs

from launch_ros.actions import Node


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    pkg_dir = get_package_share_directory('tiago_pro_bringup')

    config_locks_file = os.path.join(
        pkg_dir, 'config', 'twist_mux', 'twist_mux_locks.yaml')
    config_topics_file = os.path.join(
        pkg_dir, 'config', 'twist_mux', 'twist_mux_topics.yaml')
    joystick_file = os.path.join(
        pkg_dir, 'config', 'twist_mux', 'joystick.yaml')

    if os.environ.get('ROS_DISTRO') == 'humble':
        # Alum uses an overlaid twist_mux that can publish unstamped Twists
        # depending on launch arguments.
        cmd_vel_out = 'mobile_base_controller/cmd_vel_unstamped'
    else:
        # In cadmium and later, twist_mux publishes TwistStamped,
        # which mobile_base_controller can subscribe to directly.
        cmd_vel_out = 'mobile_base_controller/cmd_vel'

    twist_mux = include_scoped_launch_py_description(
        pkg_name='twist_mux', paths=['launch', 'twist_mux_launch.py'],
        launch_arguments={
            'cmd_vel_out': cmd_vel_out,
            'config_locks': config_locks_file,
            'config_topics': config_topics_file,
            'config_joy': joystick_file,
            'use_sim_time': launch_args.use_sim_time
        }
    )
    launch_description.add_action(twist_mux)

    twist_mux_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='twist_mux',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(pkg_dir, 'config', 'twist_mux', 'twist_mux_analyzers.yaml')
        ],
    )
    launch_description.add_action(twist_mux_analyzer)

    return


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
