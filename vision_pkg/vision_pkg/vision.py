#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class VisionProcess(Node): 
    def __init__(self):
        super().__init__("vision_process") 

        self.image_subscriber = self.create_subscription(
            Image, "image_raw", self.image_callback, 10)
        
        self.cmd_publisher = self.create_publisher(
            Twist, "cmd_vel", 10)
        self.detected_publisher = self.create_publisher(
            Twist, "detected_image", 10)
        
        self.get_logger().info("Vision started!")
    
    def image_callback(self):
        self.get_logger().info("Getting image")

def main(args=None):
    rclpy.init(args=args)
    node = VisionProcess() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()