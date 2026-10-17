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
from pathlib import Path
import tempfile


from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_param_builder import load_xacro

from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.robot_arguments import CommonArgs
from launch_pal import calibration_utils
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
    ft_sensor_teleop_left: DeclareLaunchArgument = TiagoProArgs.ft_sensor_teleop_left
    ft_sensor_teleop_right: DeclareLaunchArgument = TiagoProArgs.ft_sensor_teleop_right
    wrist_model_right: DeclareLaunchArgument = TiagoProArgs.wrist_model_right
    wrist_model_left: DeclareLaunchArgument = TiagoProArgs.wrist_model_left
    camera_model: DeclareLaunchArgument = TiagoProArgs.camera_model
    laser_model: DeclareLaunchArgument = TiagoProArgs.laser_model
    tool_changer_right: DeclareLaunchArgument = TiagoProArgs.tool_changer_right
    tool_changer_left: DeclareLaunchArgument = TiagoProArgs.tool_changer_left
    torque_estimation: DeclareLaunchArgument = TiagoProArgs.torque_estimation
    has_teleop_arms: DeclareLaunchArgument = TiagoProArgs.has_teleop_arms
    has_wrist_camera: DeclareLaunchArgument = TiagoProArgs.has_wrist_camera
    limits_v2: DeclareLaunchArgument = TiagoProArgs.limits_v2
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time
    namespace: DeclareLaunchArgument = CommonArgs.namespace
    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    calibration_tool: DeclareLaunchArgument = TiagoProArgs.calibration_tool
    wheel_model: DeclareLaunchArgument = TiagoProArgs.wheel_model
    gazebo_version: DeclareLaunchArgument = CommonArgs.gazebo_version


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(OpaqueFunction(
        function=create_robot_description_param))

    # Using ParameterValue is needed so ROS knows the parameter type
    # Otherwise https://github.com/ros2/launch_ros/issues/136
    rsp = Node(package='robot_state_publisher',
               executable='robot_state_publisher',
               output='both',
               parameters=[
                   {
                       'use_sim_time': LaunchConfiguration('use_sim_time'),
                       "robot_description": ParameterValue(
                           LaunchConfiguration("robot_description"), value_type=str
                       ),
                   }
               ],
               )

    launch_description.add_action(rsp)

    return


def create_robot_description_param(context, *args, **kwargs):

    xacro_file_path = Path(os.path.join(
        get_package_share_directory('tiago_pro_description'),
        'robots', 'tiago_pro.urdf.xacro'))

    xacro_input_args = {
        'base_type': read_launch_argument('base_type', context),
        'arm_type_right': read_launch_argument('arm_type_right', context),
        'arm_type_left': read_launch_argument('arm_type_left', context),
        'end_effector_right': read_launch_argument('end_effector_right', context),
        'end_effector_left': read_launch_argument('end_effector_left', context),
        'ft_sensor_right': read_launch_argument('ft_sensor_right', context),
        'ft_sensor_left': read_launch_argument('ft_sensor_left', context),
        'ft_sensor_teleop_right': read_launch_argument('ft_sensor_teleop_right', context),
        'ft_sensor_teleop_left': read_launch_argument('ft_sensor_teleop_left', context),
        'wrist_model_right': read_launch_argument('wrist_model_right', context),
        'wrist_model_left': read_launch_argument('wrist_model_left', context),
        'camera_model': read_launch_argument('camera_model', context),
        'laser_model': read_launch_argument('laser_model', context),
        'tool_changer_right': read_launch_argument('tool_changer_right', context),
        'tool_changer_left': read_launch_argument('tool_changer_left', context),
        'torque_estimation': read_launch_argument('torque_estimation', context),
        'calibration_tool': read_launch_argument('calibration_tool', context),
        'limits_v2': read_launch_argument('limits_v2', context),
        'use_sim_time': read_launch_argument('use_sim_time', context),
        'namespace': read_launch_argument('namespace', context),
        'is_public_sim': read_launch_argument('is_public_sim', context),
        'has_teleop_arms': read_launch_argument('has_teleop_arms', context),
        'has_wrist_camera': read_launch_argument('has_wrist_camera', context),
        'wheel_model': read_launch_argument('wheel_model', context),
        'gazebo_version': read_launch_argument('gazebo_version', context),
        'with_sc': 'true',
    }

    calibration_dir = tempfile.TemporaryDirectory()
    calibration_dir_path = Path(calibration_dir.name)

    input_dir = Path(get_package_share_directory(
        "tiago_pro_description")) / "urdf" / "calibration"

    calibration_xacro_args = calibration_utils.apply_urdf_calibration(
        input_dir, calibration_dir_path)

    xacro_input_args.update(calibration_xacro_args)

    robot_description = load_xacro(xacro_file_path, xacro_input_args)

    return [SetLaunchConfiguration('robot_description', robot_description)]


def generate_launch_description():

    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
