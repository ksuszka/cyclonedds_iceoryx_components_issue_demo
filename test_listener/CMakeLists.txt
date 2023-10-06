cmake_minimum_required(VERSION 3.5)
project(test_listener)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_auto_add_library(test_listener SHARED main.cpp)
ament_target_dependencies(test_listener rclcpp rclcpp_components)
rclcpp_components_register_nodes(test_listener "test_listener::SubscriberNode")

ament_auto_package()
