#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class AvoidenceAlgorithm(Node): 
    def __init__(self):
        super().__init__("avoidence_algorithm") 

        self.velocity_publisher = self.create_publisher(
            Twist, "cmd_vel", 10)
        
        self.sensor_subscriber = self.create_subscription(
            LaserScan, "sensor_data", self.SensorCallback, 10)
        self.get_logger().info("Avoidence algorithm started!")

    def  SensorCallback(self):
        self.get_logger().info("getting sensor data")

def main(args=None):
    rclpy.init(args=args)
    node = AvoidenceAlgorithm() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()