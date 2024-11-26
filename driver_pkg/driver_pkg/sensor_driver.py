#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_srvs.srv import SetBool

class SensorDriver(Node): 
    def __init__(self):
        super().__init__("sensor_driver") 

        self.sensor_publisher = self.create_publisher(
            LaserScan, "sensor_data", 10)
        
        self.status_service = self.create_service(
            SetBool, "sensor_status", self.SensorStatus)
        self.active = False
        self.get_logger().info("Sensor service started!")

    def SensorStatus(self, request, response):
        self.active = request.data
        if self.active:
            response.message = "Sensor active"
        else:
            response.message = "Sensor off"
        
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SensorDriver() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()