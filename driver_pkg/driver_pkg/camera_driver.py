#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import SetBool

class CameraDriver(Node): 
    def __init__(self):
        super().__init__("camera_driver") 

        self.image_publisher = self.create_publisher(
            Image, "image_raw", 10)

        self.camera_status_service = self.create_service(
            SetBool, "camera_status", self.CameraStatus)
        self.active = False
        self.get_logger().info("Camera service started!")
    
    def CameraStatus(self, request, response):
        self.active = request.data
        if self.active:
            response.message = "Camera active"
        else:
            response.message = "Camera off"
        
        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = CameraDriver() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()