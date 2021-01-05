import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from random import randint

class WiredIdPub(Node):

    def __init__(self):
        super().__init__('wired_id_pub')
        self.id_pub_ = self.create_publisher(String, 'id', 10)
        timer_period = 5.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.id = randint(0, 10000) 
    
    def timer_callback(self):
        msg = String()
        msg.data = str(self.id)
        self.id_pub_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)

    wired_laptop = WiredIdPub()
    rclpy.spin(wired_laptop)

    wired_laptop.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()