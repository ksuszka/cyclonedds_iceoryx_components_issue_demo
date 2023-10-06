from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    return LaunchDescription([
        ComposableNodeContainer(
            name="container_"+str(i),
            namespace="",
            package="rclcpp_components",
            executable="component_container",
            output="screen",
            composable_node_descriptions=[
                ComposableNode(
                    package="test_listener",
                    plugin="test_listener::SubscriberNode",
                    namespace="container_"+str(i),
                    name="listener",
                ),
            ],
        ) for i in range(0, 90)
    ])
