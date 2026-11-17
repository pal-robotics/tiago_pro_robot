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
from launch.actions import DeclareLaunchArgument, OpaqueFunction, SetLaunchConfiguration
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_pal.arg_utils import LaunchArgumentsBase, read_launch_argument
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.param_utils import merge_param_files
from launch_pal.robot_arguments import CommonArgs
from rclpy.logging import get_logger


from tiago_pro_description.launch_arguments import TiagoProArgs
from tiago_pro_description.tiago_pro_launch_utils import get_tiago_pro_hw_suffix


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    arm_type_right: DeclareLaunchArgument = TiagoProArgs.arm_type_right
    arm_type_left: DeclareLaunchArgument = TiagoProArgs.arm_type_left
    end_effector_right: DeclareLaunchArgument = TiagoProArgs.end_effector_right
    end_effector_left: DeclareLaunchArgument = TiagoProArgs.end_effector_left
    wrist_model_right: DeclareLaunchArgument = TiagoProArgs.wrist_model_right
    wrist_model_left: DeclareLaunchArgument = TiagoProArgs.wrist_model_left
    has_teleop_arms: DeclareLaunchArgument = TiagoProArgs.has_teleop_arms
    use_sim_time:  DeclareLaunchArgument = CommonArgs.use_sim_time


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):
    play_motion2 = include_scoped_launch_py_description(
        pkg_name='play_motion2',
        paths=['launch', 'play_motion2.launch.py'],
        launch_arguments={
            'use_sim_time':  launch_args.use_sim_time,
            'motions_file': LaunchConfiguration('motions_file'),
            'motion_planner_config': LaunchConfiguration('motion_planner_config')
        })

    launch_description.add_action(OpaqueFunction(
        function=create_play_motion_filename))
    launch_description.add_action(play_motion2)

    return


def create_play_motion_filename(context):

    pkg_name = 'tiago_pro_bringup'
    pkg_share_dir = get_package_share_directory(pkg_name)
    has_teleop_arms = read_launch_argument('has_teleop_arms', context)
    ee_right = read_launch_argument('end_effector_right', context)
    ee_left = read_launch_argument('end_effector_left', context)
    arm_right = read_launch_argument('arm_type_right', context)
    arm_left = read_launch_argument('arm_type_left', context)
    wrist_model_right = read_launch_argument('wrist_model_right', context)
    wrist_model_left = read_launch_argument('wrist_model_left', context)

    hw_suffix = get_tiago_pro_hw_suffix(
        arm_right=arm_right,
        arm_left=arm_left,
        end_effector_right=ee_right,
        end_effector_left=ee_left,
    )

    # Determine the necessary motions
    ee_motions = []
    motions_folder = os.path.join(pkg_share_dir, 'config', 'motions')
    base_motions_file = 'tiago_pro_motions_no_arms.yaml'

    if 'short-wrist' in (wrist_model_right, wrist_model_left):
        get_logger('play_motion2').warning(
            "The 'short-wrist' model is not supported for play_motion2. "
            'Loaded motions will not include arm movements.')
    elif wrist_model_right != wrist_model_left:
        get_logger('play_motion2').error(
            'Wrist models must be the same for both arms')
    # both arms
    elif arm_right != 'no-arm' and arm_left != 'no-arm':
        base_motions_file = 'tiago_pro_motions_general_'+wrist_model_right+'.yaml'
    # right arm only
    elif arm_right != 'no-arm' and arm_left == 'no-arm':
        base_motions_file = 'tiago_pro_motions_general_arm_right.yaml'
    # left arm only
    elif arm_right == 'no-arm' and arm_left != 'no-arm':
        base_motions_file = 'tiago_pro_motions_general_arm_left.yaml'

    if ee_left != 'no-end-effector' and arm_left != 'no-arm':
        ee_motions.append(f'tiago_pro_motions_{ee_left}_left.yaml')
    if ee_right != 'no-end-effector' and arm_right != 'no-arm':
        ee_motions.append(f'tiago_pro_motions_{ee_right}_right.yaml')
    if has_teleop_arms:
        ee_motions.append('tiago_pro_motions_teleop_arms.yaml')

    head_pkg = get_package_share_directory('tiago_pro_head_bringup')

    head_motions = [os.path.join(head_pkg, 'config', 'motions',
                                 'head_motions.yaml')]

    motion_files = [base_motions_file]
    motion_files.extend(ee_motions)

    motion_yamls = [os.path.join(motions_folder, f) for f in motion_files]
    motion_yamls.extend(head_motions)

    # Safety check for not throwing error if some file does not exist
    for f in motion_yamls.copy():
        if not os.path.exists(f):
            get_logger('play_motion2').warning(f"Motion file '{f}' does not exist. Skipping...")
            motion_yamls.remove(f)

    combined_yaml = merge_param_files(motion_yamls)
    motion_planner_file = f'motion_planner{hw_suffix}.yaml'

    if has_teleop_arms == 'True':
        motion_planner_file = f'motion_planner{hw_suffix}_teleop-arms.yaml'

    motion_planner_config = PathJoinSubstitution([
        pkg_share_dir,
        'config', 'motion_planner', motion_planner_file])

    return [SetLaunchConfiguration('motions_file', combined_yaml),
            SetLaunchConfiguration('motion_planner_config', motion_planner_config)]


def generate_launch_description():
    # Create the launch description
    ld = LaunchDescription()

    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld
