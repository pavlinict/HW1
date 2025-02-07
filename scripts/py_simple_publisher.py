#!/usr/bin/env python3

#print('I am alive!')
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import String
from dis_tutorial1.msg import CustomMessage  
import random

""" def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("py_simple_publisher_node")
    
    publisher = node.create_publisher(String, "/chat", 10)
    
    message = String()
    message_same = "Hello world of ROS2 publishers! This is message number: "
    message_num = 3

    while rclpy.ok():
        message.data = message_same + str(message_num)
        publisher.publish(message)
        message_num += 1

        node.get_logger().info("Publisher: I performed one iteration!")
        time.sleep(1)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main() """

class MyPublisherNode(Node):
    def __init__(self):
        super().__init__('my_publisher_node')
        self.publisher = self.create_publisher(CustomMessage, '/chat', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.publish_message)
        self.message_id = 0

    def publish_message(self):
        msg = CustomMessage()
        msg.content = 'Hello, ROS 2!'
        msg.id = self.message_id
        msg.my_bool = bool(random.getrandbits(1))  # Randomly selected boolean
        self.publisher.publish(msg)
        self.get_logger().info('Published: {}'.format(msg))
        self.message_id += 1

def main(args=None):
    rclpy.init(args=args)
    node = MyPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()