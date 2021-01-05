from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='wired_rpi_test',
            namespace='rpi',
            executable='wired_id_pub',
            name='wired_rpi'
        )
    ])