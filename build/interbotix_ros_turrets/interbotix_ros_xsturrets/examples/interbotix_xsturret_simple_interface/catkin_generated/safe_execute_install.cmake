execute_process(COMMAND "/home/ben/interbotix_ws/build/interbotix_ros_turrets/interbotix_ros_xsturrets/examples/interbotix_xsturret_simple_interface/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ben/interbotix_ws/build/interbotix_ros_turrets/interbotix_ros_xsturrets/examples/interbotix_xsturret_simple_interface/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
