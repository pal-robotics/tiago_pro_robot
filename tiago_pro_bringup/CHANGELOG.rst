^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.5.1 (2026-08-17)
------------------
* New boxing position
* Contributors: Rafa Rojas

2.5.0 (2026-07-21)
------------------
* pre grasp motions
* Contributors: matteovillani

2.4.1 (2026-06-17)
------------------

2.4.0 (2026-06-05)
------------------

2.3.0 (2026-05-21)
------------------

2.2.5 (2026-04-24)
------------------
* reduce gripper motion for open from 0.079 to 0.07
* Contributors: ileniaperrella

2.2.4 (2026-04-20)
------------------

2.2.3 (2026-04-20)
------------------

2.2.2 (2026-04-13)
------------------

2.2.1 (2026-04-13)
------------------

2.2.0 (2026-04-10)
------------------
* Add arguments to support the new gazebo
* Contributors: thomaspeyrucain

2.1.3 (2026-04-08)
------------------

2.1.2 (2026-03-31)
------------------
* Remove init
* Contributors: Aina

2.1.1 (2026-03-24)
------------------

2.1.0 (2026-03-19)
------------------
* Add support for short-wrist
* Contributors: Noel Jimenez

2.0.1 (2026-03-19)
------------------
* Add safety incrementer controller + reduce increment to be able to close more
* Contributors: thomas.peyrucain

2.0.0 (2026-03-05)
------------------
* Add pal configuration
* Switch to pal_joy + fix flake
* Update Joystick Layout
* Contributors: thomaspeyrucain

1.36.3 (2026-02-26)
-------------------

1.36.2 (2026-02-26)
-------------------

1.36.1 (2026-02-24)
-------------------
* change boxing teleop motion
* Contributors: susannamastromauro

1.36.0 (2026-02-18)
-------------------

1.35.4 (2026-02-10)
-------------------
* adding calibration_tool param
* Contributors: silviamasiello

1.35.3 (2026-02-09)
-------------------
* add boxing motion for teleop station
* fix param bug
* Contributors: ileniaperrella, matteovillani

1.35.2 (2026-02-05)
-------------------
* delete teleop end effectors
* fix play_motion2
* add enable wrist camera option
* Contributors: ileniaperrella

1.35.1 (2026-02-03)
-------------------
* remove whitespace pipeline
* fix condition in the play_motion2 teleop
* Contributors: ileniaperrella

1.35.0 (2026-02-02)
-------------------
* modify motion for last joint
* add motion planning for tleeop arms
* change motions file for teleop
* update modules with ee_teleop
* add test for xacro
* add end_effector_teleop_right and end_effector_teleop_left in files
* update play_motion2 namespace
* add motion for teleop task
* add ft sensor on teleop arms
* add modules and fix default controllers
* add motions for teleop arms (usable only with skip_planning)
* add teleop args
* Contributors: ileniaperrella

1.34.3 (2026-01-28)
-------------------

1.34.2 (2026-01-27)
-------------------

1.34.1 (2026-01-08)
-------------------
* Add torso motions with no arms
* Contributors: Aina

1.34.0 (2025-12-15)
-------------------

1.33.0 (2025-12-05)
-------------------

1.32.3 (2025-11-28)
-------------------
* fixing values
* changing values motions
* Contributors: susannamastromauro

1.32.2 (2025-11-12)
-------------------
* changing max and mid value
* changing gripper values motion
* fixing gripper limits
* Contributors: susannamastromauro

1.32.1 (2025-11-03)
-------------------

1.32.0 (2025-10-23)
-------------------
* Add play_motion2 cli dependency
* Contributors: Isaac Acevedo

1.31.2 (2025-10-21)
-------------------

1.31.1 (2025-10-13)
-------------------
* preparing pkg for public release
* Contributors: andreacapodacqua

1.31.0 (2025-08-27)
-------------------

1.30.1 (2025-08-05)
-------------------
* Merge branch 'tpe/update_gripper_range' into 'humble-devel'
  Update close motion for pal pro gripper
  See merge request robots/tiago_pro_robot!153
* Update close motion for pal pro gripper
* Contributors: thomaspeyrucain

1.30.0 (2025-08-01)
-------------------
* launch the module not bringup.launch
* typo
* checking for EE to be pal-pro-gripper
* moving the side logic
* deviding launch file to better dbeug and handle different gripper type
* add gripper_grasper module
* Contributors: Matteo Villani

1.29.5 (2025-08-01)
-------------------
* Sim adding boxing motion
* Contributors: silviamasiello

1.29.4 (2025-07-18)
-------------------
* Fix home sides motions to updateit as the home motion
* Add explore motion
* Add reach motions
* Add reach up motion
* Contributors: Aina

1.29.3 (2025-07-16)
-------------------
* Add remappings for removing robot_description namespace
* Contributors: Noel Jimenez

1.29.2 (2025-07-10)
-------------------

1.29.1 (2025-07-10)
-------------------
* Add namespace to safe_command_node instances
* Add safe_command to joystick analyzers
* Contributors: Noel Jimenez

1.29.0 (2025-07-08)
-------------------
* Add diagnostic analyzers
* Contributors: Noel Jimenez

1.28.0 (2025-06-18)
-------------------
* Adapt to changes in play_motion2
* Contributors: davidfernandez

1.27.1 (2025-06-17)
-------------------

1.27.0 (2025-06-06)
-------------------

1.26.4 (2025-06-05)
-------------------

1.26.3 (2025-06-05)
-------------------

1.26.2 (2025-06-04)
-------------------

1.26.1 (2025-06-03)
-------------------
* Merge branch 'air/fix/head_motions' into 'humble-devel'
  Remove head motions
  See merge request robots/tiago_pro_robot!132
* Remove head motions
* Contributors: Aina, thomaspeyrucain

1.26.0 (2025-05-29)
-------------------
* Better calibration motions
* Launching the SEA broadcaster and basic calibration movements
* Contributors: oscarmartinez

1.25.8 (2025-05-28)
-------------------

1.25.7 (2025-05-19)
-------------------

1.25.6 (2025-05-08)
-------------------

1.25.5 (2025-05-02)
-------------------

1.25.4 (2025-04-17)
-------------------
* Add motion file for allegro and rebase
* Add motion planner files with allegro
* Add allegro hand on moveit configuration
* Add allegro hand as a possible end effector
* Contributors: Aina

1.25.3 (2025-04-03)
-------------------
* Add missing home motions for single arm
* Contributors: David ter Kuile

1.25.2 (2025-04-02)
-------------------

1.25.1 (2025-03-31)
-------------------

1.25.0 (2025-03-27)
-------------------
* Support for SEA in the bringup
* Contributors: oscarmartinez

1.24.0 (2025-03-25)
-------------------
* removed marker_vel
* added tab_vel to twist_mux
* Contributors: andreacapodacqua

1.23.4 (2025-03-25)
-------------------
* Restructure joystick config files
* Contributors: Aina

1.23.3 (2025-03-18)
-------------------

1.23.2 (2025-02-28)
-------------------

1.23.1 (2025-02-27)
-------------------
* Fix boxing for spherical wrist
* Contributors: Aina

1.23.0 (2025-02-24)
-------------------
* update locks and topics to integrate assisted_teleop
* Contributors: andreacapodacqua

1.22.2 (2025-02-18)
-------------------

1.22.1 (2025-01-23)
-------------------

1.22.0 (2025-01-22)
-------------------
* lock robot if charging
* Contributors: antoniobrandi

1.21.0 (2025-01-16)
-------------------
* Merge branch 'tpe/simplify-3d-model' into 'humble-devel'
  Tpe/simplify 3d model
  See merge request robots/tiago_pro_robot!104
* Remove has_tray argument
* Contributors: thomas.peyrucain, thomaspeyrucain

1.20.0 (2025-01-07)
-------------------
* Remove unused base_type argument
* Remove unused robot_name argument
* Contributors: Noel Jimenez

1.19.0 (2024-12-10)
-------------------
* Remove safety-eps form torso and update boxing motion
* Contributors: David ter Kuile

1.18.0 (2024-12-02)
-------------------
* Add head motions
* Add prefix to pm2 module
* Remove camera model as parameter for pm2 launch file
* Keep camera in tiago pro
* Remove camera model as arg
* Change head controller path
* Contributors: Aina

1.17.0 (2024-11-21)
-------------------
* Apply elif condition
* Fix enter between planning_groups & exclude_from_planning_joints
* Remove unneeded planning groups
* Contributors: Aina

1.16.0 (2024-11-08)
-------------------

1.15.0 (2024-11-06)
-------------------
* Fixing pipeline
* Adding safe command to joystick
* Contributors: vivianamorlando

1.14.2 (2024-11-06)
-------------------
* Disable torso control with joystick
* Contributors: David ter Kuile

1.14.1 (2024-10-30)
-------------------
* Merge branch 'air/fix/motions' into 'humble-devel'
  Fix home motion for straight wrist
  See merge request robots/tiago_pro_robot!90
* Add head joints
* Fix home motion for straight wrist
* Contributors: Aina, thomaspeyrucain

1.14.0 (2024-10-29)
-------------------
* Add wrist models to play_motion2 module
* Contributors: Noel Jimenez

1.13.0 (2024-10-29)
-------------------

1.12.1 (2024-10-28)
-------------------

1.12.0 (2024-10-28)
-------------------
* Put back safety controller for the torso + change motions
* Contributors: thomas.peyrucain

1.11.0 (2024-10-25)
-------------------

1.10.1 (2024-10-22)
-------------------
* Merge branch 'tpe/fix_head' into 'humble-devel'
  Tpe/fix head
  See merge request robots/tiago_pro_robot!81
* Add boxing and fix home
* Update torso up and down and the specific motions for each arm
* Add 2 different files for motions depending on the writst
* Contributors: Aina, thomaspeyrucain

1.10.0 (2024-10-21)
-------------------
* Add new home to arm right and left
* change home motion as boxing
* Contributors: Aina

1.9.0 (2024-10-11)
------------------
* Revert to previous home motion
* Contributors: thomas.peyrucain

1.8.2 (2024-10-02)
------------------
* Merge branch 'tpe/fix_wrist' into 'humble-devel'
  update motions with new wrist
  See merge request robots/tiago_pro_robot!75
* update motions with new wrist
* Contributors: thomas.peyrucain, thomaspeyrucain

1.8.1 (2024-09-27)
------------------
* Merge branch 'tpe/limit_update' into 'humble-devel'
  Update pal_sea_arm to add the joint reflect + update the home motion
  See merge request robots/tiago_pro_robot!74
* Update pal_sea_arm to add the joint reflect + update the home motion
* Contributors: thomas.peyrucain, thomaspeyrucain

1.8.0 (2024-09-19)
------------------
* New launch args
* Support for removable tray
* Contributors: oscarmartinez

1.7.0 (2024-09-12)
------------------

1.6.0 (2024-09-10)
------------------
* Add slash to node names on parameter files
* Remove the unnecesary ft_sensor arguments in bringup
* Remove ft_sensor from play_motion related files
* Remove ft_sensor related in joy_teleop
* Remove ft_sensor from HW specific config generation
* Contributors: Noel Jimenez, oscarmartinez

1.5.0 (2024-08-29)
------------------
* Refactor mobile_base_controller launch
* Contributors: David ter Kuile

1.4.0 (2024-08-22)
------------------
* Adapted so it is the same as tiago dual
* Suggested changes
* Added play motion module
* Suggested changes
* Hardware specific motions with grippers
* Contributors: oscarmartinez

1.3.0 (2024-08-08)
------------------

1.2.0 (2024-08-07)
------------------

1.1.0 (2024-08-05)
------------------
* enabled y-axis base movements
* Fix path
* Fix default device
* Contributors: andreacapodacqua, thomas.peyrucain

1.0.13 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

1.0.12 (2024-06-27)
-------------------

1.0.11 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/tiago_pro_robot!50
* Change import for launch args
* Merge branch 'dtk/fix/joystick-driver' into 'humble-devel'
  Add new joy_linux node
  See merge request robots/tiago_pro_robot!45
* Add joy linux to launch file
* Add new joy_linux node
* Contributors: David ter Kuile, davidterkuile

1.0.10 (2024-05-22)
-------------------

1.0.9 (2024-05-09)
------------------

1.0.8 (2024-04-26)
------------------

1.0.7 (2024-04-18)
------------------
* Merge branch 'dtk/fix/play-motion2-dependency' into 'humble-devel'
  Add dependency of play_motion2
  See merge request robots/tiago_pro_robot!37
* Add dependency of play_motion2
* Merge branch 'omm/feat/public_sim_check' into 'humble-devel'
  Public Sim check
  See merge request robots/tiago_pro_robot!36
* is_public_sim support in launch files
* Contributors: Oscar, davidterkuile

1.0.6 (2024-04-17)
------------------

1.0.5 (2024-04-16)
------------------
* Merge branch 'dtk/feat/add-modules' into 'humble-devel'
  Dtk/feat/add modules
  See merge request robots/tiago_pro_robot!32
* fix teleop config file paths and names
* Fix argument typo in joy_teleop
* Add modules
* Contributors: David ter Kuile, Noel Jimenez

1.0.4 (2024-04-10)
------------------

1.0.3 (2024-03-26)
------------------

1.0.2 (2024-03-26)
------------------
* Merge branch 'dtk/fix/fix-nav-topic' into 'humble-devel'
  Dtk/fix/fix nav topic
  See merge request robots/tiago_pro_robot!29
* Change twist mux navigation topic
* Add missing sim time to twist mux
* Contributors: David ter Kuile, andreacapodacqua

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/tiago_pro_robot!28
* update copyright year
* Add missnig use sim time arg
* Update motion name
* Disable gripper specific motions
* update config files
* Add regen_em script
* Restructure launch file tiago_pro_bringup
* Merge branch 'fix/rename_approach_planner' into 'humble-devel'
  Rename approach_planner config to motion_planner
  See merge request robots/tiago_pro_robot!25
* Rename approach_planner config to motion_planner
* Merge branch 'fix/update_approach_planner_config' into 'humble-devel'
  Update approach_planner configuration
  See merge request robots/tiago_pro_robot!24
* Update approach_planner configuration
* Contributors: David ter Kuile, Jordan Palacios, Noel Jimenez, davidterkuile

1.0.0 (2024-01-30)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/tiago_pro_robot!23
* fix twist_mux config name
* simplify joy_telop launch file (as done for tiago and ari)
* update to 3.8 the cmake_minimum_required Version
* twist mux and joytelop added - to check
* update launch files with launch_pal structure
* update motions yaml file
* migration launch files
* CMakeLists and package files
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.0.11 (2023-11-08)
-------------------

0.0.10 (2023-10-20)
-------------------
* Merge branch 'change_name' into 'master'
  Change tiago_v2_prototype to tiago_pro + move arm to an external package
  See merge request robots/tiago_pro_robot!16
* Change tiago_v2_prototype to tiago_pro + move arm to an external package
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.9 (2023-05-25)
------------------
* Merge branch 'fix_home' into 'master'
  new home gripper 7
  See merge request robots/tiago_pro_robot!11
* no alive motions
* new home gripper 7
* Contributors: Aina, Sai Kishor Kothakota

0.0.8 (2023-05-24)
------------------
* Merge branch 'wbc_per_arm' into 'master'
  Wbc per arm
  See merge request robots/tiago_pro_robot!10
* added the motion tiago_dancing_happy
* Contributors: Sai Kishor Kothakota

0.0.7 (2023-05-24)
------------------

0.0.6 (2023-05-24)
------------------
* Merge branch 'fix_motions' into 'master'
  Fix motions
  See merge request robots/tiago_pro_robot!7
* modified home motion so the arms won't need to support on base covers on poweroff
* new home_right/left and gripper fixed on tiago_dancing
* no meta descriptio
* alie_fixed and home joint 7
* offer and shake
* Contributors: Aina, Sai Kishor Kothakota

0.0.5 (2023-05-22)
------------------

0.0.4 (2023-05-20)
------------------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_pro_robot!6
* added the new home motion and review the torso heights
* fix up the main motions for stress testing
* Don't start actuator pid controllers and position controllers by default, and handle it by an application
* remove joy_teleop from bringup and use startup as the incrementer server is timing out with delay in deployer
* comment out the robot pose publisher until the navigation is setup
* added more motions generated by aina
* launch Move group for motion planning
* load the pre-defined motions in the play_motion launch file
* added some generic motion configuration on the TIAGo2 Robot
* Contributors: Sai Kishor Kothakota

0.0.3 (2023-05-16)
------------------
* Merge branch 'play_motion_fixes' into 'master'
  play motion fixes
  See merge request robots/tiago_pro_robot!4
* add play_motion to the bringup launch
* added head joints in the exclude from planning joints list
* Contributors: Sai Kishor Kothakota, ileniaperrella

0.0.2 (2023-05-16)
------------------

0.0.1 (2023-05-16)
------------------
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_pro_robot!1
* Merge branch 'play-motion' into 'new_v2_bringup'
  Play motion
  See merge request robots/tiago_pro_robot!3
* update the actuator PID values for the whole arm
* added play_motion launch files
* Launch actuator pid controller and load its configuration
* Fix broken path
* added the bringup package and the configuration
* Contributors: Jordan Palacios, Sai Kishor Kothakota, ileniaperrella
