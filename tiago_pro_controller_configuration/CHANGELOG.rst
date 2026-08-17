^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.5.1 (2026-08-17)
------------------

2.5.0 (2026-07-21)
------------------
* Control by default the grasping frame
* Fixing pipeline
* fixing pep8
* Adding use_grasping_frame for cartesian controller
* Contributors: matteovillani, vivianamorlando

2.4.1 (2026-06-17)
------------------
* ci/cd test
* ci/cd errors
* defined argument to spawn a subset of tsid controllers specified in the list at the beginning of the launch file
* Contributors: francescodorazio

2.4.0 (2026-06-05)
------------------

2.3.0 (2026-05-21)
------------------

2.2.5 (2026-04-24)
------------------

2.2.4 (2026-04-20)
------------------
* modify the launch and config file in order to use correctly the chained
  impedance
* Contributors: ileniaperrella

2.2.3 (2026-04-20)
------------------

2.2.2 (2026-04-13)
------------------

2.2.1 (2026-04-13)
------------------
* Fixing open loop param
* Contributors: vivianamorlando

2.2.0 (2026-04-10)
------------------
* Fix indentation
* Fix lint
* Rollback is teleop arg
* Contributors: vivianamorlando

2.1.3 (2026-04-08)
------------------
* fix identation
* use same wrist model for teleop arms
* Adding torso in config file of cartesian controller
* Contributors: ileniaperrella, vivianamorlando

2.1.2 (2026-03-31)
------------------

2.1.1 (2026-03-24)
------------------
* Fix dependencies condition
* Remove cache + fix flake8
* change paths for yaml
* add dependency to package.xml
* launch and config file of impedance controller
* Contributors: sofieblankers, thomas.peyrucain, vivianamorlando

2.1.0 (2026-03-19)
------------------
* Do not launch torque estimation controllers with short-wrist
* Add support for short-wrist
* Contributors: Noel Jimenez

2.0.1 (2026-03-19)
------------------

2.0.0 (2026-03-05)
------------------

1.36.3 (2026-02-26)
-------------------

1.36.2 (2026-02-26)
-------------------

1.36.1 (2026-02-24)
-------------------

1.36.0 (2026-02-18)
-------------------

1.35.4 (2026-02-10)
-------------------

1.35.3 (2026-02-09)
-------------------

1.35.2 (2026-02-05)
-------------------
* delete teleop end effectors
* Contributors: ileniaperrella

1.35.1 (2026-02-03)
-------------------

1.35.0 (2026-02-02)
-------------------
* change name from teleop_basestation to pilot_station
* delete not necessary PIDs (to retune)
* delete cartesian force not used
* update modules with ee_teleop
* add test for xacro
* add grippers actuators pids to improve ctrl
* remove not used params in cartesian forc ctrl
* add end_effector_teleop_right and end_effector_teleop_left in files
* add basestation urdf
* add pids yaml for gripper
* Adding haptic feeback info to params
* add motion for teleop task
* add cartesian controller for teleop left arm
* add gravity compensation teleop left and right
* add modules and fix default controllers
* add teleop args
* Contributors: ileniaperrella, vivianamorlando

1.34.3 (2026-01-28)
-------------------
* correcting gains
* rm unused file
* Contributors: vivianamorlando

1.34.2 (2026-01-27)
-------------------

1.34.1 (2026-01-08)
-------------------
* Add "Hardware Components Activity" module dependency
* Contributors: Noel Jimenez

1.34.0 (2025-12-15)
-------------------

1.33.0 (2025-12-05)
-------------------

1.32.3 (2025-11-28)
-------------------

1.32.2 (2025-11-12)
-------------------

1.32.1 (2025-11-03)
-------------------

1.32.0 (2025-10-23)
-------------------

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

1.30.0 (2025-08-01)
-------------------

1.29.5 (2025-08-01)
-------------------

1.29.4 (2025-07-18)
-------------------

1.29.3 (2025-07-16)
-------------------

1.29.2 (2025-07-10)
-------------------
* Fix missing quote for tsid_default_controllers module
* Contributors: Noel Jimenez

1.29.1 (2025-07-10)
-------------------

1.29.0 (2025-07-08)
-------------------

1.28.0 (2025-06-18)
-------------------

1.27.1 (2025-06-17)
-------------------
* Temporal fix for torso tolerance
* Contributors: Aina Irisarri

1.27.0 (2025-06-06)
-------------------

1.26.4 (2025-06-05)
-------------------

1.26.3 (2025-06-05)
-------------------

1.26.2 (2025-06-04)
-------------------
* Adding conditions to properly start the SEA broadcaster
* Contributors: oscarmartinez

1.26.1 (2025-06-03)
-------------------

1.26.0 (2025-05-29)
-------------------
* Adding check to the broadcaster
* Adding missing launch of the gravity controller in torque mode
* Launching the SEA broadcaster and basic calibration movements
* Contributors: oscarmartinez

1.25.8 (2025-05-28)
-------------------
* reduce to 1cm
* update trajectory tolerance
* update torso controller with trajectory constraint
* fix pipeline
* delete whitespace
* fix whitespace
* add cartesian vel diff local frame
* update manipulation cube
* update x of the manipulation cube
* update gains for joint_space_controller_vel
* update gains for cartesian velocity
* remove torso_lift_joint for cartesian controller
* fix name from triago to tiagopro
* update yaml with new gains and namespaces
* separate cartesian_vel gains
* add manipulation cube
* update tsid_default_controllers launch file
* update gains
* Fix typo in module
* Add torso joint space controller
* Add tsid controllers dependency
* Rename torso param files
* Add tsid controllers module
* Add launch file to load tsid controllers
* Add tsid controller param files, templated
* fix tiago pro instead of triago
* add forward velocity control for the arms
* Contributors: David ter Kuile, ileniaperrella

1.25.7 (2025-05-19)
-------------------
* Merge branch 'omm/inertia_shaping_controllers' into 'humble-devel'
  Launching the inertia shaping controllers if torque_estimation enabled
  See merge request robots/tiago_pro_robot!125
* Linters
* Launching the inertia shaping controllers if torque_estimation enabled
* Contributors: oscarmartinez, thomaspeyrucain

1.25.6 (2025-05-08)
-------------------

1.25.5 (2025-05-02)
-------------------

1.25.4 (2025-04-17)
-------------------
* Add motion file for allegro and rebase
* Add allegro hand controller
* Contributors: Aina

1.25.3 (2025-04-03)
-------------------
* Simplify gravity compensation
* Remove unused param files
* Contributors: David ter Kuile

1.25.2 (2025-04-02)
-------------------

1.25.1 (2025-03-31)
-------------------
* Simplify arm controllers
* Contributors: David ter Kuile

1.25.0 (2025-03-27)
-------------------
* Adding proper module config
* Support for SEA in the controllers
* Contributors: oscarmartinez

1.24.0 (2025-03-25)
-------------------

1.23.4 (2025-03-25)
-------------------

1.23.3 (2025-03-18)
-------------------
* Remove unused imu broadcaster
* Contributors: David ter Kuile

1.23.2 (2025-02-28)
-------------------

1.23.1 (2025-02-27)
-------------------

1.23.0 (2025-02-24)
-------------------

1.22.2 (2025-02-18)
-------------------

1.22.1 (2025-01-23)
-------------------

1.22.0 (2025-01-22)
-------------------

1.21.0 (2025-01-16)
-------------------

1.20.0 (2025-01-07)
-------------------

1.19.0 (2024-12-10)
-------------------

1.18.0 (2024-12-02)
-------------------
* Add head controller
* Change head controller path
* Contributors: Aina

1.17.0 (2024-11-21)
-------------------

1.16.0 (2024-11-08)
-------------------
* Remove unused arm config files
  Config files are taken from pal_sea_arm on its launcher
* Contributors: Noel Jimenez

1.15.0 (2024-11-06)
-------------------
* update motor torque constant for pal-pro-gripper (temporary)
* Contributors: ileniaperrella

1.14.2 (2024-11-06)
-------------------

1.14.1 (2024-10-30)
-------------------

1.14.0 (2024-10-29)
-------------------
* add gravity compensation dependency
* Contributors: ileniaperrella

1.13.0 (2024-10-29)
-------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

1.12.1 (2024-10-28)
-------------------

1.12.0 (2024-10-28)
-------------------

1.11.0 (2024-10-25)
-------------------
* fix typo
* update params for gravity compensation
* delete wrong joint impedance controller
* open loop arg set as true
* add dependency for omni_base_controller_configuration
* Contributors: ileniaperrella

1.10.1 (2024-10-22)
-------------------
* Merge branch 'fix/gravity-spawn' into 'humble-devel'
  Use Unless condition on the load of gravity compensation
  See merge request robots/tiago_pro_robot!78
* Use Unless condition on the load of gravity compensation
* Merge branch 'air/feat/arm_controllers' into 'humble-devel'
  Change back the arm controllers into the default controllers
  See merge request robots/tiago_pro_robot!79
* Change back the arm controllers into the default controllers
* Contributors: Aina, ileniaperrella, thomaspeyrucain

1.10.0 (2024-10-21)
-------------------
* load gravity as default controller (only params)
* Contributors: ileniaperrella

1.9.0 (2024-10-11)
------------------

1.8.2 (2024-10-02)
------------------

1.8.1 (2024-09-27)
------------------

1.8.0 (2024-09-19)
------------------

1.7.0 (2024-09-12)
------------------

1.6.0 (2024-09-10)
------------------
* set head controller to perform open loop control
* Contributors: lorenzoferrini

1.5.0 (2024-08-29)
------------------
* Refactor mobile_base_controller launch
* Contributors: David ter Kuile

1.4.0 (2024-08-22)
------------------
* Add confif file for mobile base from omni_base package
* Contributors: Aina

1.3.0 (2024-08-08)
------------------
* Change arm controllers launch to the arm_controller launch file
* fix usi_sim_condition
* Add arm default controller launch file and module
* Add arm_controller launch file
* Add condition for arms controllers
* Contributors: Aina

1.2.0 (2024-08-07)
------------------
* Use controller_type from the controllers config
* Contributors: Noel Jimenez

1.1.0 (2024-08-05)
------------------
* update gravity compensation conf file
* fix typo on reduction_ratio param
* root link changed
* controller name not the same as defined in the launch file
* Remove use_stamped_vel parameter
* Contributors: Noel Jimenez, ileniaperrella

1.0.13 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* change module name into 20\_*
* Contributors: Aina, Noel Jimenez

1.0.12 (2024-06-27)
-------------------
* Merge branch 'dtk/fix-gazebo-urdf' into 'humble-devel'
  Dtk/fix gazebo urdf
  See merge request robots/tiago_pro_robot!51
* Add imu sensor broadcaster
* Contributors: David ter Kuile, davidterkuile

1.0.11 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/tiago_pro_robot!50
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

1.0.10 (2024-05-22)
-------------------

1.0.9 (2024-05-09)
------------------

1.0.8 (2024-04-26)
------------------

1.0.7 (2024-04-18)
------------------

1.0.6 (2024-04-17)
------------------

1.0.5 (2024-04-16)
------------------
* Merge branch 'dtk/feat/add-modules' into 'humble-devel'
  Dtk/feat/add modules
  See merge request robots/tiago_pro_robot!32
* Remove gravity_compensation_controller
* Change module number prefix to 10
* Add modules
* Contributors: David ter Kuile, Noel Jimenez, davidterkuile

1.0.4 (2024-04-10)
------------------
* Add ros2controlcli dependency
* Contributors: Noel Jimenez

1.0.3 (2024-03-26)
------------------

1.0.2 (2024-03-26)
------------------

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/tiago_pro_robot!28
* update copyright year
* Add conditional launch for mobile base controller
* Remove unused imports for flake test
* Add missing bracked
* Restructure launch files controller_configuration
* Merge branch 'dtk/fix/add-hector-gazebo-plugin' into 'humble-devel'
  Add force_based_move gazebo plugin for omni base
  See merge request robots/tiago_pro_robot!27
* fix linters
* added hector_gazebo_plugin dep and disabled mobile base controller in simulation
* Merge branch 'dtk/fix/camera-simulation' into 'humble-devel'
  Dtk/fix/camera simulation
  See merge request robots/tiago_pro_robot!26
* Update linter issues
* integrate mobile_base_controller
* Contributors: David ter Kuile, andreacapodacqua, davidterkuile, ileniaperrella

1.0.0 (2024-01-30)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/tiago_pro_robot!23
* Migrate to new version of gravity_compensation_controller
* fix depend name
* remote type of the controllers in the yaml (not necessary already in
  the launch)
* adding missing dep
* duplicated file
* update to 3.8 the cmake_minimum_required Version
* delete export not needed
* update launch files with launch_pal structure
* migration launch files
* CMakeLists and package files
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

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
