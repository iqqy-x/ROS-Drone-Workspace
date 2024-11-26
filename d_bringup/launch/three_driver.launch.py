from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    camera_service_node = Node(
        package = "driver_pkg",
        executable = "camera_driver"
    )

    grip_service_node = Node(
        package = "driver_pkg",
        executable = "grip_driver"
    )

    sensor_service_node = Node(
        package = "driver_pkg",
        executable = "sensor_driver"
    )

    ld.add_action(camera_service_node)
    ld.add_action(grip_service_node)
    ld.add_action(sensor_service_node)

    return ld