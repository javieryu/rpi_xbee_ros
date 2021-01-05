from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='wired_rpi_test',
            namespace='laptop',
            executable='wired_laptop',
            name='wired_test'
        )
    ])