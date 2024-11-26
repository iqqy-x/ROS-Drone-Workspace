#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class Mavros(Node): 
    def __init__(self):
        super().__init__("mavros")  
        
        self.publisher = self.create_subscription(
            Imu, "telem_msg", self.ImuCallback, 10)
        self.get_logger().info("Mavros started!")
    
    def ImuCallback(self):
        self.get_logger().info("Getting imu")

def main(args=None):
    rclpy.init(args=args)
    node = Mavros() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()