#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from HW1.msg import CustomMessage
""" 
mynode = None

def topic_callback(msg):
    global mynode
    mynode.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    global mynode
    rclpy.init(args=args)
    mynode = rclpy.create_node("py_simple_subscriber_node")
    
    subscription = mynode.create_subscription(String, "/chat", topic_callback, 10)

    while rclpy.ok():
        rclpy.spin_once(mynode)

    mynode.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main() """

class MySubscriberNode(Node):
    def __init__(self):
        super().__init__('my_subscriber_node')
        self.subscription = self.create_subscription(
            CustomMessage,
            '/chat',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info('Received: {} {} {}'.format(msg.content, msg.id, msg.my_bool))

def main(args=None):
    rclpy.init(args=args)
    node = MySubscriberNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()