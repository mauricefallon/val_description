cmake_minimum_required(VERSION 2.8.3)
project(val_description)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  xacro 
  rospy
)

catkin_package(
 CATKIN_DEPENDS xacro rospy
)

set(urdf_files "")


set(PATH_TO_ROBOTS_MODEL ${CMAKE_CURRENT_SOURCE_DIR}/model/robots)
set(PATH_TO_ROBOTS_INSTANCE ${CMAKE_CURRENT_SOURCE_DIR}/instance/instances/robots)

# Xacro files
file(GLOB model_xacro_files ${PATH_TO_ROBOTS_MODEL}/common/*/*.xacro ${PATH_TO_ROBOTS_MODEL}/valkyrie_A/*/*.xacro ${PATH_TO_ROBOTS_MODEL}/valkyrie_B/*/*.xacro)
file(GLOB instance_xacro_files ${PATH_TO_ROBOTS_INSTANCE}/xacro/*/*.xacro)

# Robot files
file(GLOB urdf_xacro_files ${PATH_TO_ROBOTS_MODEL}/*.xacro)
file(GLOB instance_xacro_files ${PATH_TO_ROBOTS_INSTANCE}/*.xacro)

set(URDF_OUTPUT_PATH ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/model/urdf)
set(INSTANCE_OUTPUT_PATH ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/instance/instances/instance_files)

message(${CATKIN_PACKAGE_SHARE_DESTINATION})

# Create output directories
file(MAKE_DIRECTORY ${URDF_OUTPUT_PATH})
file(MAKE_DIRECTORY ${INSTANCE_OUTPUT_PATH})

# Generate urdf's and put them in the /model/urdf directory
foreach(it ${urdf_xacro_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  message("processing urdf file :" ${basepath}/${basename})

  set(expanded_file "${URDF_OUTPUT_PATH}/${basename}.urdf")
  message("produce expanded file :" ${expanded_file})

  xacro_add_xacro_file(${it} ${expanded_file})
  
  set(urdf_files ${urdf_files} ${expanded_file})
endforeach(it)


foreach(it ${instance_xacro_files})
  get_filename_component(basepath ${it} PATH)
  get_filename_component(basename ${it} NAME_WE)

  message("processing xml file :" ${basepath}/${basename})

  set(expanded_file "${INSTANCE_OUTPUT_PATH}/${basename}.xml")
  message("produce expanded file :" ${expanded_file})

  xacro_add_xacro_file(${it} ${expanded_file})
  
  set(instance_files ${instance_files} ${expanded_file})
endforeach(it)

catkin_python_setup()

catkin_add_nosetests(test)

add_custom_target(val_description_media_files ALL DEPENDS ${urdf_files} ${instance_files})

# install urdf and xacro files
install(DIRECTORY model
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY instance
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY ${URDF_OUTPUT_PATH}
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/model
)

install(DIRECTORY ${INSTANCE_OUTPUT_PATH}
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/instance/instances)
