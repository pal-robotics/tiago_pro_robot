^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Merge branch 'tpe/fix_motions' into 'master'
  Update motions with the new arm sign change + fix controllers
  See merge request robots/tiago_pro_robot!22
* update gravity constants & impedance
* Add is_simulation in the default controller to spawn different controllers on simulation than on the real robot
* remove arm controllers from default controllers
* added advanced grasping launch arguments
* Update motions with the new arm sign change + fix controllers
* Contributors: Adria Roig, ileniaperrella, sergiacosta, thomas.peyrucain

0.0.12 (2023-11-16)
-------------------

0.0.11 (2023-11-08)
-------------------
* Merge branch 'smooth_position_control' into 'master'
  Smooth position control
  See merge request robots/tiago_pro_robot!20
* Modify parameters for direct_position_control
* Add parameters for direct_position_control
* Contributors: Adria Roig, Sai Kishor Kothakota

0.0.10 (2023-10-20)
-------------------
* Merge branch 'change_name' into 'master'
  Change tiago_v2_prototype to tiago_pro + move arm to an external package
  See merge request robots/tiago_pro_robot!16
* Change tiago_v2_prototype to tiago_pro + move arm to an external package
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.9 (2023-05-25)
------------------

0.0.8 (2023-05-24)
------------------
* Merge branch 'wbc_per_arm' into 'master'
  Wbc per arm
  See merge request robots/tiago_pro_robot!10
* added the wbc_controllers launch to controller configuration
* fix direct_control adding more args to control separately arm left and arm right
* moved the direct_control launch to launch folder
* Contributors: Sai Kishor Kothakota, ileniaperrella

0.0.7 (2023-05-24)
------------------
* update the impedance gains on the robot
* Contributors: Sai Kishor Kothakota

0.0.6 (2023-05-24)
------------------
* Merge branch 'gravity_compensation_per_arm' into 'master'
  added another launch file for gravity compensation where with the arg side it...
  See merge request robots/tiago_pro_robot!9
* load the parameters of the gravity compnesation with ros_bringup
* make gravity_compensation_controller per arm launch more generic
* added another launch file for gravity compensation where with the arg side it is possible to 1 arm instead of both
* Merge branch 'impedance-controllers' into 'master'
  Impedance controllers
  See merge request robots/tiago_pro_robot!8
* increase the timeout of the imepdance controllers
* remove the start of gripper controllers
* impedance kp kd updated
* fix config file directory
* updated actuators params for gravity compensation
* impedance controllers files for both arms
* gripper controllers added
* Merge branch 'fix_motions' into 'master'
  Fix motions
  See merge request robots/tiago_pro_robot!7
* Update the acceleration and velocity limits for the mobile base controller
* Contributors: Sai Kishor Kothakota, ileniaperrella

0.0.5 (2023-05-22)
------------------
* added timeout to the joint_state_controller
* Contributors: Sai Kishor Kothakota

0.0.4 (2023-05-20)
------------------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_pro_robot!6
* added the missing head_action dependency
* Don't start actuator pid controllers and position controllers by default, and handle it by an application
* added the point head action to the default controllers launch file
* load the mobile_base_controller and increase the timeout to 300 seconds
* Contributors: Sai Kishor Kothakota

0.0.3 (2023-05-16)
------------------

0.0.2 (2023-05-16)
------------------

0.0.1 (2023-05-16)
------------------
* Added gravity compensation controller dependency
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_pro_robot!1
* Added head_controller to joint_trajectory_controllers.yaml
* Merge branch 'play-motion' into 'new_v2_bringup'
  Play motion
  See merge request robots/tiago_pro_robot!3
* update the motor torque constants to proper values
* delete files copied from canopies pkgs
* Merge branch 'gripper-integration' into 'new_v2_bringup'
  Grippers integration
  See merge request robots/tiago_pro_robot!2
* gripper controller params set in the current pkg
* controller added for grippers
* grippers robotiq-2f-85 added for both arms
* Update the motor torque constants for the left and the right arm
* Update the robot model chaines for the gravity compensation controller
* remove the invalid torso_yaw_joint configuration
* reenable right_7_joint
* Disabling arm right 7 temporarily
* Adding missing arm controllers
* added the configuration of the gravity compenesation from canopies configuration
* added the bringup package and the configuration
* update for new arms placement
* Add arm controllers
* First commit
* Contributors: Jordan Palacios, Luca Marchionni, Narcis Miguel, Sai Kishor Kothakota, ileniaperrella
