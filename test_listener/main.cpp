#include "rclcpp/rclcpp.hpp"
#include "rclcpp_components/register_node_macro.hpp"

namespace test_listener
{
  class SubscriberNode : public rclcpp::Node
  {
  public:
    SubscriberNode(rclcpp::NodeOptions options)
      : Node("subscriber_node", rclcpp::NodeOptions(options)
          .start_parameter_services(false)
          .start_parameter_event_publisher(false))
    {
    }
  };
}

RCLCPP_COMPONENTS_REGISTER_NODE(test_listener::SubscriberNode)
