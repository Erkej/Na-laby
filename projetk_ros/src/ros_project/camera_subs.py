#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2
import numpy as np

class camera_subs(Node):
    def __init__(self):
        super().__init__('camera_subscriber')
        self.window_name = "camera"

        self.bridge = CvBridge()
        self.publisher_ = self.create_publisher(Point, '/point', 10)

        self.subscription = self.create_subscription(
            Image, '/image_raw', self.listener_callback, 10
        )

        self.qr = cv2.QRCodeDetector()
        self.last_pub = 0.0  # proste ograniczenie spamowania

        cv2.namedWindow(self.window_name)

    def listener_callback(self, image_data):
        # ROS -> OpenCV
        try:
            frame = self.bridge.imgmsg_to_cv2(image_data, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"CvBridge error: {e}")
            return

        # QR detect
        data, points, _ = self.qr.detectAndDecode(frame)

        if points is not None and len(points) > 0:
            pts = points.astype(int).reshape(-1, 2)
            cv2.polylines(frame, [pts], True, (255, 0, 0), 2)

            cx = float(np.mean(pts[:, 0]))
            cy = float(np.mean(pts[:, 1]))

            if data:
                cv2.putText(frame, f"QR: {data}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

            p = Point()
            p.x = cx
            p.y = cy
            p.z = 0.0
            self.publisher_.publish(p)

            cv2.circle(frame, (int(cx), int(cy)), 6, (0, 255, 0), -1)

        cv2.imshow(self.window_name, frame)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = camera_subs()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
