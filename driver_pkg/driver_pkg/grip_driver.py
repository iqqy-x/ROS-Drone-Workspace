#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_srvs.srv import SetBool

class GripDriver(Node): 
    def __init__(self):
        super().__init__("grip_driver") 

        self.status_publisher = self.create_publisher(
            Bool, "status_pwr", 10)
        
        self.status_service = self.create_service(
            SetBool, "grip_status", self.GripStatus)
        self.active = False
        self.get_logger().info("Grip service started!")
        
    def GripStatus(self, request, response):
        self.active = request.data
        if self.active:
            response.message = "Grip active"
        else:
            response.message = "Grip off"
        
        self.get_logger().info(response.message)
        return response
        

def main(args=None):
    rclpy.init(args=args)
    node = GripDriver() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()