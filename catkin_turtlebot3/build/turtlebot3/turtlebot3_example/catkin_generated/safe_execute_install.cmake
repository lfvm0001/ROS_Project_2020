execute_process(COMMAND "/home/jose/ROS_Project_2020/catkin_turtlebot3/build/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jose/ROS_Project_2020/catkin_turtlebot3/build/turtlebot3/turtlebot3_example/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
