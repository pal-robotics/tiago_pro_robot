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


def get_tiago_pro_hw_suffix(
    arm_right: str = 'no-arm',
    arm_left: str = 'no-arm',
    end_effector_right: str = 'no-end-effector',
    end_effector_left: str = 'no-end-effector',
    ft_sensor_right: str = 'no-ft-sensor',
    ft_sensor_left: str = 'no-ft-sensor',
    ft_sensor_teleop_right: str = 'no-ft-sensor',
    ft_sensor_teleop_left: str = 'no-ft-sensor',
    has_teleop_arms: bool = False,
):
    """
    Generate a substitution that creates a text suffix combining the specified \
    tiago pro arguments.

    The arguments are read as string
    """
    right_suffix = get_single_arm_hw_suffix(
        arm_right, end_effector_right, ft_sensor_right
    )
    left_suffix = get_single_arm_hw_suffix(arm_left, end_effector_left, ft_sensor_left)

    suffix = left_suffix + right_suffix
    return suffix


def get_single_arm_hw_suffix(
        arm: str = 'no-arm',
        end_effector: str = 'no-ee',
        ft_sensor: str = 'no-ft-sensor'):
    """
    Generate a substitution that creates a text suffix combining the specified tiago pro arguments.

    The arguments are read as string

    For instance, the suffix for: arm=tiago-pro, end_effector='pal-pro-gripper', ft_sensor='rokubi'
    would be '_pal-pro-gripper_rokubi'
    """
    if arm in ['no-arm']:
        suffix = arm
        return '_' + suffix

    end_effector = 'no-ee' if end_effector == 'no-end-effector' else end_effector

    components = []
    components.append(end_effector)

    if ft_sensor != 'no-ft-sensor':
        components.append(ft_sensor)

    suffix = '_' + '_'.join(components)
    return suffix
