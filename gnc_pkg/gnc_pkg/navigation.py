#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from std_srvs.srv import SetBool

class NavigationProcess(Node): 
    def __init__(self):
        super().__init__("navigation_process") 

        self.subscriber = self.create_subscription(
            Twist, "cmd_vel", self.VelocityCallback, 10)
        
        self.publisher = self.create_publisher(
            Imu, "telem_msg", 10)

        self.camera_client = self.create_client(
            SetBool, "camera_status")
        self.grip_client = self.create_client(
            SetBool, "grip_status")
        self.sensor_client = self.create_client(
            SetBool, "sensor_status")
        
        clients = [self.camera_client, self.grip_client, self.sensor_client]
        
        for client in clients:
             while not client.wait_for_service(timeout_sec=1.0):
                 self.get_logger().info(f"Waiting for driver status service...")

    def VelocityCallback(self):
        self.get_logger().info("Getting velocity")
    
    def DriverRequest(self, driver):
        request = SetBool.Request()
        request.data = True

        if driver == "Camera":
            self.camera_client.call_async(request)
            self.get_logger().info("Camera driver requested to activate")
        elif driver == "Grip":
            self.grip_client.call_async(request)
            self.get_logger().info("Grip driver requested to activate")
        elif driver == "Sensor":
            self.sensor_client.call_async(request)
            self.get_logger().info("Sensor driver requested to activate")
        else:
            self.get_logger().info("Driver not found")

def main(args=None):
    rclpy.init(args=args)
    node = NavigationProcess() 

    while rclpy.ok():
        driver_option = input("Camera, Grip, or Sensor : ")
        if driver_option in ["Camera", "Grip", "Sensor"]:
            node.DriverRequest(driver_option)
        else:
            node.get_logger().info("Invalid driver input!")

    rclpy.shutdown()

if __name__ == "__main__":
    main()