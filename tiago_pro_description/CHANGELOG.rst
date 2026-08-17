^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.5.1 (2026-08-17)
------------------

2.5.0 (2026-07-21)
------------------

2.4.1 (2026-06-17)
------------------
* frequency of ros2_controllers in simulation from 100Hz to 1kHz
* Contributors: francescodorazio

2.4.0 (2026-06-05)
------------------
* revert d435 camera in robot configuration
* Contributors: ileniaperrella

2.3.0 (2026-05-21)
------------------
* added option d435i as default
* Contributors: martinaannicelli

2.2.5 (2026-04-24)
------------------

2.2.4 (2026-04-20)
------------------

2.2.3 (2026-04-20)
------------------
* Remove gazebo plugins from the hardware side
* Contributors: Noel Jimenez

2.2.2 (2026-04-13)
------------------
* Add the type string due the issue that is not yet fixed in this release
* Contributors: thomas.peyrucain

2.2.1 (2026-04-13)
------------------

2.2.0 (2026-04-10)
------------------
* Fix jobs
* Add safety controller to prevent the torso to get stuck in simulation with a small epsilon
* Add arguments to support the new gazebo
* Contributors: thomaspeyrucain

2.1.3 (2026-04-08)
------------------

2.1.2 (2026-03-31)
------------------

2.1.1 (2026-03-24)
------------------

2.1.0 (2026-03-19)
------------------
* Add support for short-wrist
* Contributors: Noel Jimenez

2.0.1 (2026-03-19)
------------------

2.0.0 (2026-03-05)
------------------

1.36.3 (2026-02-26)
-------------------
* Adding new wheel_type grassland. Used in the ethercat system
* Contributors: Jordan Palacios

1.36.2 (2026-02-26)
-------------------
* Add support for no-wheels
* Contributors: Jordan Palacios

1.36.1 (2026-02-24)
-------------------

1.36.0 (2026-02-18)
-------------------
* Fix coma
* Add new limits values
* Add new parameter for the limits
* Contributors: Aina

1.35.4 (2026-02-10)
-------------------
* adding calibration_tool param
* Contributors: silviamasiello

1.35.3 (2026-02-09)
-------------------
* fix param bug
* Contributors: matteovillani

1.35.2 (2026-02-05)
-------------------
* test fix
* fix pipeline
* fix test identation
* delete teleop end effectors
* add enable wrist camera option
* Contributors: ileniaperrella

1.35.1 (2026-02-03)
-------------------

1.35.0 (2026-02-02)
-------------------
* fix inertia for basestation
* update end effector camera base link (typo)
* change name from teleop_basestation to pilot_station
* reset calibration_offset
* offsets for tp28
* add camera to the wrist
* update modules with ee_teleop
* fix test allegro hand descr
* fix test args
* exclude allegro-hand for testing
* add test for xacro
* add end_effector_teleop_right and end_effector_teleop_left in files
* add basestation urdf
* fix FT sensors after rebase
* rm non existing directory
* add ft ros2 control
* add ft sensor on teleop arms
* fix urdf
* add modules and fix default controllers
* fix joint reflect
* add teleop args
* add teleop arms in the urdf
* Contributors: ileniaperrella, vivianamorlando

1.34.3 (2026-01-28)
-------------------
* Add parameter expose_safety_interface
* Contributors: Noel Jimenez

1.34.2 (2026-01-27)
-------------------
* Add parameter expose_collision_interface
* Contributors: Noel Jimenez

1.34.1 (2026-01-08)
-------------------
* rename calibration directory
* Contributors: silviamasiello

1.34.0 (2025-12-15)
-------------------
* changes for head_offset
* changes for head_offset
* changes for head_offset
* changes for head_offset
* head_offset
* reduction param
* reduction param
* offset
* offset
* offset
* adding head calibration offset
* adding head calibration offset
* Contributors: silviamasiello

1.33.0 (2025-12-05)
-------------------
* Add gazebo_version xacro argument
* Contributors: Noel Jimenez

1.32.3 (2025-11-28)
-------------------

1.32.2 (2025-11-12)
-------------------
* changing max and mid value
* changing max and mid value
* Contributors: susannamastromauro

1.32.1 (2025-11-03)
-------------------
* Fix humble tests excluding allegro hand end-effector
* Contributors: Noel Jimenez

1.32.0 (2025-10-23)
-------------------

1.31.2 (2025-10-21)
-------------------
* Add urdf calibration args for the arm
* Remove tiago pro controller config dependency
* Contributors: Aina Irisarri, David ter Kuile

1.31.1 (2025-10-13)
-------------------
* preparing pkg for public release
* Contributors: andreacapodacqua

1.31.0 (2025-08-27)
-------------------
* remove realsense overlay
* Contributors: antoniobrandi

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

1.29.1 (2025-07-10)
-------------------

1.29.0 (2025-07-08)
-------------------

1.28.0 (2025-06-18)
-------------------

1.27.1 (2025-06-17)
-------------------

1.27.0 (2025-06-06)
-------------------
* Uniform namespace
* Contributors: antoniobrandi

1.26.4 (2025-06-05)
-------------------
* Remove imu
* Change sensors paths according to pal_urdf_utils
* Change path for imu ros2 control urdf
* Change path for ftsensor ros2_control xacro
* Contributors: Aina, Aina Irisarri

1.26.3 (2025-06-05)
-------------------
* Enabling idle_mode_on_stop for ethercat system
* Removing trailing spaces
* Contributors: Jordan Palacios

1.26.2 (2025-06-04)
-------------------

1.26.1 (2025-06-03)
-------------------

1.26.0 (2025-05-29)
-------------------

1.25.8 (2025-05-28)
-------------------

1.25.7 (2025-05-19)
-------------------

1.25.6 (2025-05-08)
-------------------
* Enable error_protection
* Contributors: Jordan Palacios

1.25.5 (2025-05-02)
-------------------
* Update file ros2_control.urdf.xacro
* Change can bus for allegro right
* Contributors: Aina Irisarri

1.25.4 (2025-04-17)
-------------------
* Delete for now xela components
* Add dependency for allegro description
* Add allegro hand as a possible end effector
* add velocity command interface for the torso
* Contributors: Aina, ileniaperrella

1.25.3 (2025-04-03)
-------------------

1.25.2 (2025-04-02)
-------------------
* Create ethercat system even if there are no arms
* Contributors: Noel Jimenez

1.25.1 (2025-03-31)
-------------------

1.25.0 (2025-03-27)
-------------------
* Adding proper module config
* Support for SEA in tiago_pro_description
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
* Merge branch 'tpe/add_inertia_version' into 'humble-devel'
  Add parameter for the new arm
  See merge request robots/tiago_pro_robot!106
* Add parameter for the new arm
* Contributors: thomas.peyrucain, thomaspeyrucain

1.23.1 (2025-02-27)
-------------------
* Change default config of TIAGo Pro
* Contributors: thomas.peyrucain

1.23.0 (2025-02-24)
-------------------

1.22.2 (2025-02-18)
-------------------
* Merge branch 'tpe/add_d455' into 'humble-devel'
  Add Realsense D455 to tiago pro head
  See merge request robots/tiago_pro_robot!109
* Add Realsense D455 to tiago pro head
* Contributors: thomas.peyrucain, thomaspeyrucain

1.22.1 (2025-01-23)
-------------------
* Merge branch 'tpe/simplify_3d_models' into 'humble-devel'
  Fix naming + change collision toroso_fixed
  See merge request robots/tiago_pro_robot!108
* Fix naming + change collision toroso_fixed
* Contributors: thomas.peyrucain, thomaspeyrucain

1.22.0 (2025-01-22)
-------------------

1.21.0 (2025-01-16)
-------------------
* Merge branch 'tpe/simplify-3d-model' into 'humble-devel'
  Tpe/simplify 3d model
  See merge request robots/tiago_pro_robot!104
* Scale sligthly the visual of the base_link of the torso to remove visualization bug + add visual for the head_link
* Fix test
* Add simplyfied models
* Remove has_tray argument
* Contributors: thomas.peyrucain, thomaspeyrucain

1.20.0 (2025-01-07)
-------------------

1.19.0 (2024-12-10)
-------------------
* Remove safety-eps form torso and update boxing motion
* Contributors: David ter Kuile

1.18.0 (2024-12-02)
-------------------
* Remove camera model as parameter for pm2 launch file
* Add camera model as parameter to check in head urdf
* Keep camera in tiago pro
* Rebase on head fixes
* Fix ros2 control macro for tiago_head
* Remove camera model arg from tiago_pro_robot
* Remove camera model and add tiago_pro_head dependency
* Change head meshes to tiago_pro_head package
* Contributors: Aina

1.17.0 (2024-11-21)
-------------------

1.16.0 (2024-11-08)
-------------------
* Remove mistake on ros2_control xacro
* Contributors: Aina Irisarri

1.15.0 (2024-11-06)
-------------------

1.14.2 (2024-11-06)
-------------------
* set rw rate less than 200 to avoid spam and ros2control errors
* Contributors: ileniaperrella

1.14.1 (2024-10-30)
-------------------

1.14.0 (2024-10-29)
-------------------

1.13.0 (2024-10-29)
-------------------

1.12.1 (2024-10-28)
-------------------
* Merge branch 'vmo/inertias' into 'humble-devel'
  Modifying inertia of torso
  See merge request robots/tiago_pro_robot!86
* Modifying inertia of torso
* Contributors: thomaspeyrucain, vivianamorlando

1.12.0 (2024-10-28)
-------------------
* Put back safety controller for the torso + change motions
* Update torso limits
* Contributors: Aina, thomas.peyrucain

1.11.0 (2024-10-25)
-------------------
* delete CAN ros2_control for torso_lift
* Add xacro tests
* Contributors: Aina, ileniaperrella

1.10.1 (2024-10-22)
-------------------
* Merge branch 'tpe/fix_head' into 'humble-devel'
  Tpe/fix head
  See merge request robots/tiago_pro_robot!81
* Fix head position
* Contributors: thomas.peyrucain, thomaspeyrucain

1.10.0 (2024-10-21)
-------------------

1.9.0 (2024-10-11)
------------------
* Add reflect on the 5th joint
* Contributors: thomas.peyrucain

1.8.2 (2024-10-02)
------------------

1.8.1 (2024-09-27)
------------------
* Merge branch 'tpe/limit_update' into 'humble-devel'
  Update pal_sea_arm to add the joint reflect + update the home motion
  See merge request robots/tiago_pro_robot!74
* Update pal_sea_arm to add the joint reflect + update the home motion
* Merge branch 'omm/missing_module_args' into 'humble-devel'
  Added missing module arg
  See merge request robots/tiago_pro_robot!73
* Added missing module arg
* Contributors: oscarmartinez, thomas.peyrucain, thomaspeyrucain

1.8.0 (2024-09-19)
------------------
* Tests passing
* Std gripper orientation
* Suggested changes
* Support for multiple FT sensors at the same time
* Added wrist_model and tool_changer args
* Removing repeated arm
* Support for removable tray
* Added head
* Added torso
* Support for new old arm naming
* added frames for sellion and eyes
* Invert head 2 joint direction
* Contributors: David ter Kuile, ferrangebelli, oscarmartinez

1.7.0 (2024-09-12)
------------------
* Disable ros2_control_tiago_pro_system_ethercat if no arms
* Contributors: Noel Jimenez

1.6.0 (2024-09-10)
------------------
* Add slash to node names on parameter files
* Restored full hw suffix for future compatibility
* Remove ft_sensor from HW specific config generation
* Contributors: Noel Jimenez, oscarmartinez

1.5.0 (2024-08-29)
------------------

1.4.0 (2024-08-22)
------------------

1.3.0 (2024-08-08)
------------------

1.2.0 (2024-08-07)
------------------
* Set different read/write rates for hardware components
  https://github.com/ros-controls/ros2_control/pull/1570
* Contributors: Noel Jimenez

1.1.0 (2024-08-05)
------------------
* Split ros2_control hardware into three RobotControl components
* Contributors: Noel Jimenez

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
* Change occurences of sim_time to use_sim_time
* Move remove global gazebo.urdf file
* Contributors: David ter Kuile, davidterkuile

1.0.11 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Change import for launch args
  See merge request robots/tiago_pro_robot!50
* Add is missing is_multiple xacro arg
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

1.0.10 (2024-05-22)
-------------------
* Merge branch 'dtk/fix/head-camera-name' into 'humble-devel'
  Change camera name and topic to head_front_camera
  See merge request robots/tiago_pro_robot!40
* Change camera name and topic to head_front_camera
* Merge branch 'smd/feat/realsense_calibrated' into 'humble-devel'
  Added calibrated tf realsense for the real robot
  See merge request robots/tiago_pro_robot!42
* Added calibrated tf realsense for the real robot
* Contributors: David ter Kuile, davidterkuile, sergiomoyano

1.0.9 (2024-05-09)
------------------
* Merge branch 'omm/feat/arm_name_std' into 'humble-devel'
  Changed arm_model to arm_type in the URDF
  See merge request robots/tiago_pro_robot!39
* Changed arm_model to arm_type in the URDF
* Contributors: davidterkuile, oscarmartinez

1.0.8 (2024-04-26)
------------------
* Fix typo
* Contributors: davidterkuile

1.0.7 (2024-04-18)
------------------
* Merge branch 'omm/feat/public_sim_check' into 'humble-devel'
  Public Sim check
  See merge request robots/tiago_pro_robot!36
* is_public_sim support in launch files
* urdf support for is_public_sim
* Merge branch 'omm/fix/urdf_proper_structure' into 'humble-devel'
  Robot urdf reestructured
  See merge request robots/tiago_pro_robot!35
* Loading calibration constants properly
* Robot urdf reestructured
* Contributors: Oscar, davidterkuile

1.0.6 (2024-04-17)
------------------
* Merge branch 'omm/fix/default_laser' into 'humble-devel'
  Fixed default laser value
  See merge request robots/tiago_pro_robot!34
* Small reorganization of the urdf
* Changed default laser
* Applying autoformater
* Contributors: Oscar, davidterkuile

1.0.5 (2024-04-16)
------------------
* Merge branch 'fix/ros-planar-move-rate' into 'humble-devel'
  modified gazebo ros_planar_move rate
  See merge request robots/tiago_pro_robot!33
* modified gazebo ros_planar_move rate
* Merge branch 'dtk/feat/add-modules' into 'humble-devel'
  Dtk/feat/add modules
  See merge request robots/tiago_pro_robot!32
* Change module number prefix to 10
* Add modules
* Merge branch 'omm/fix/spinning_tiago' into 'humble-devel'
  Restored ros_planar_move plugin
  See merge request robots/tiago_pro_robot!31
* Restored ros_planar_move plugin
* Contributors: David ter Kuile, Noel Jimenez, Oscar, andreacapodacqua, davidterkuile

1.0.4 (2024-04-10)
------------------

1.0.3 (2024-03-26)
------------------
* Add missing realsense simulation dependency
* Contributors: David ter Kuile

1.0.2 (2024-03-26)
------------------

1.0.1 (2024-03-22)
------------------
* Merge branch 'dtk/fix/restructure' into 'humble-devel'
  Dtk/fix/restructure
  See merge request robots/tiago_pro_robot!28
* update copyright year
* Remove unsupported lidars from test
* Add missing realsense2_description dependency
* Add missing robot_state_publisher dependency
* Add missing controller_configuration dependency
* Update supported lasers in urdf
* Add hw_suffix python module for tiago-pro-description
* Add URDF tests
* Restructure URDF
* Choose to spawn the arms or not in the urdf
* Avoid bug that is unable to parse colon with spac ein urdf
* Remove arm meshes
* Merge branch 'dtk/fix/add-hector-gazebo-plugin' into 'humble-devel'
  Add force_based_move gazebo plugin for omni base
  See merge request robots/tiago_pro_robot!27
* Create a pal_distro dependency to not break humble ci untill pr gets accepted
* added hector_gazebo_plugin dep and disabled mobile base controller in simulation
* Add force_based_move gazebo plugin for omni base
* Merge branch 'dtk/fix/camera-simulation' into 'humble-devel'
  Dtk/fix/camera simulation
  See merge request robots/tiago_pro_robot!26
* Add realsense camera in head
* integrate mobile_base_controller
* fix gripper name
* fix on the ft_sensor type
* Contributors: David ter Kuile, andreacapodacqua, davidterkuile, ileniaperrella

1.0.0 (2024-01-30)
------------------
* Merge branch 'ros2-migration' into 'humble-devel'
  Ros2 migration
  See merge request robots/tiago_pro_robot!23
* Fix lintern tests
* remove files not used
* fix misaligned
* fix gripper name
* delete extra choices for the robot_name
* update to 3.8 the cmake_minimum_required Version
* update deg_to_rad file extension
* python module not needed
* update launch files with launch_pal structure
* migration launch files
* urdf migration
* meshes/ rviz config
* CMakeLists and package files
* config files
* migration of CMakeLists.txt and package.xml to ros2
* Contributors: Adria Roig, ileniaperrella

0.0.11 (2023-11-08)
-------------------

0.0.10 (2023-10-20)
-------------------
* Merge branch 'fix/ft_naming' into 'master'
  Change arm_ft\_ to wrist_ft to match TIAGo
  See merge request robots/tiago_pro_robot!19
* Change arm_ft\_ to wrist_ft to match TIAGo
* remove deg_to_rad to make use of pal_urdf_utils package
* Merge branch 'change_name' into 'master'
  Change tiago_v2_prototype to tiago_pro + move arm to an external package
  See merge request robots/tiago_pro_robot!16
* Update package.xml
* Change tiago_v2_prototype to tiago_pro + move arm to an external package
* Contributors: Jordan Palacios, thomaspeyrucain

0.0.9 (2023-05-25)
------------------

0.0.8 (2023-05-24)
------------------
* Merge branch 'wbc_per_arm' into 'master'
  Wbc per arm
  See merge request robots/tiago_pro_robot!10
* Flipped the limits of the head
* Contributors: Sai Kishor Kothakota

0.0.7 (2023-05-24)
------------------

0.0.6 (2023-05-24)
------------------

0.0.5 (2023-05-22)
------------------

0.0.4 (2023-05-20)
------------------
* Merge branch 'flip_arm_link_3' into 'master'
  remove joy_teleop from bringup and use startup as the incrementer server is...
  See merge request robots/tiago_pro_robot!6
* added realsense2_description dependency
* added head_screen_link to the URDF
* Merge branch 'head-camera' into 'flip_arm_link_3'
  Head camera integration
  See merge request robots/tiago_pro_robot!5
* intel d435 added
* 180 degrees flip of link 3 to improve motion ranges
* Contributors: Luca Marchionni, Sai Kishor Kothakota, ileniaperrella

0.0.3 (2023-05-16)
------------------

0.0.2 (2023-05-16)
------------------
* remove unused tiago_sea_arm_description dependency
* Contributors: Sai Kishor Kothakota

0.0.1 (2023-05-16)
------------------
* Merge branch 'new_v2_bringup' into 'master'
  New v2 bringup and urdf
  See merge request robots/tiago_pro_robot!1
* Added gazebo flags for joint and reformat dynamic parameters for ars, head and torso
* remove log file
* Reduce head joint limits and update dynamic parameters
* Flip joint_2 limits
* Merge branch 'gripper-integration' into 'new_v2_bringup'
  Grippers integration
  See merge request robots/tiago_pro_robot!2
* grippers robotiq-2f-85 added for both arms
* update joint position limtis
* removed not used mesh folders
* Install gazebo directory too
* Cleaning and simplification of collision meshes
* fixed inertia and joints naming
* both arms fixed and tool link added
* First v2 proto alsmost working version
* update for new arms placement
* test manipulability with moveit and workspace
* Configuration with arm in the front and pointing down
* Added params for arm placement and params in launch files
* Mounting pose of the arms in an external file
* Update rviz config file
* Use reflect param
* Add gazebo plugins
* First commit
* Contributors: Jordan Palacios, Luca Marchionni, Narcis Miguel, Sai Kishor Kothakota, ileniaperrella
