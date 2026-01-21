import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    usb_cam_cfg = os.path.join(
        get_package_share_directory("ros_project"),
        'config',
        'params.yaml'
    )
    return LaunchDescription([
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            # arguments=["/src/src/fake_came.png"], 
            parameters=[{
                'video_device': '/dev/video0',   
                'image_width': 640,
                'image_height': 480,
                'pixel_format': 'yuyv',         
            }],
            remappings=[('image_raw', '/image_raw')],
            output='screen'

        ),
       Node(
            package='ros_project',
            executable='camera_subs',
            name='camera_subs'
        ),
        Node(
            package='ros_project',
            executable='robot_cont',
            name='robot_cont',
            output='screen'
        )
    ])