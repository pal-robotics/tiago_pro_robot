^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_pro_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.12 (2023-11-16)
-------------------
* Merge branch 'fixed_torso_argument_pro' into 'master'
  added fixed torso argument to TIAGo pro
  See merge request robots/tiago_pro_robot!21
* added fixed torso argument to TIAGo pro
* Contributors: Sai Kishor Kothakota

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
