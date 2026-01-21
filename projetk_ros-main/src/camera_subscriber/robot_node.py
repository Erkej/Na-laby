#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

class robot_node(Node):
    def __init__(self):
        super().__init__('robot_controler')
        self.window_name = "robot_controler"
        self.subscription = self.create_subscription(Point,'/point',self.listener_callback,10)
        self.subscription 
        self.publisher_ = self.create_publisher(JointTrajectory, "/joint_trajectory_controller/joint_trajectory", 10)
        self.traj = JointTrajectory()
        self.traj.joint_names = [
            'shoulder_pan_joint',
            'shoulder_lift_joint',
            'elbow_joint',
            'wrist_1_joint',
            'wrist_2_joint',
            'wrist_3_joint'
        ]
        self.go_up = False
    def listener_callback(self, msg):
        if msg.y < 256:
            self.go_up = True
        else:
            self.go_up = False
        self.move_robot()
        

    def move_robot(self):
        point = JointTrajectoryPoint()
        point.time_from_start = Duration(sec=4, nanosec=0)
        point.positions = [0.0, -1.57, 0.0, -1.57, 0.0, 0.0] if self.go_up else [0.0, -0.2, 0.0, -1.0, 0.0, 0.0]
        self.traj.points = [point]
        self.publisher_.publish(self.traj)

def main(args=None):
    rclpy.init(args=args)
    node2 = robot_node()
    rclpy.spin(node2)
    node2.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()