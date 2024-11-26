#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist

class GUIStatus(Node): 
    def __init__(self):
        super().__init__("gui_status") 

        self.sensor_subscriber = self.create_subscription(
            LaserScan, "sensor_data", self.SensorCallback, 10)
        self.status_power_subscriber = self.create_subscription(
            Bool, "status_pwr", self.StatusPowerCallback, 10)
        self.velocity_subscriber = self.create_subscription(
            Twist, "cmd_vel", self.VelocityCallback, 10)
        self.image_subscriber = self.create_subscription(
            Image, "detected_image", self.ImageCallback, 10)
        
        self.get_logger().info("GUI status started!")

    def SensorCallback(self):
        self.get_logger().info("Getting data sensor")
    def StatusPowerCallback(self):
        self.get_logger().info("Getting power status")
    def VelocityCallback(self):
        self.get_logger().info("Getting data velocity")
    def ImageCallback(self):
        self.get_logger().info("Getting image")


def main(args=None):
    rclpy.init(args=args)
    node = GUIStatus() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()