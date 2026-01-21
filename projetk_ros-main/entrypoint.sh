#!/bin/bash
set -e
cd /ros2_ws
source /opt/ros/humble/setup.sh
mkdir /ros2_ws/src
cd /ros2_ws/src
ros2 pkg create camera_subscriber --build-type ament_python --dependencies cv_bridge python3-opencv sensor_msgs geometry_msgs trajectory_msgs
cp /src/src/camera_subscriber/robot_node.py /ros2_ws/src/camera_subscriber/camera_subscriber/robot_node.py
cp /src/src/camera_subscriber/camera_node.py /ros2_ws/src/camera_subscriber/camera_subscriber/camera_node.py
mkdir /ros2_ws/src/camera_subscriber/launch
cp /src/src/camera_subscriber/launch/start.launch.py /ros2_ws/src/camera_subscriber/launch/start.launch.py
cp /src/src/camera_subscriber/setup.py  /ros2_ws/src/camera_subscriber/setup.py

cd /ros2_ws
colcon build
source ./install/setup.sh
ros2 launch ur_robot_driver ur_control.launch.py \
    ur_type:=ur5 \
    robot_ip:=yyy.yyy.yyy.yyy \
    use_fake_hardware:=true \
    launch_rviz:=true \
    initial_joint_controller:=joint_trajectory_controller &
ros2 launch camera_subscriber start.launch.py &

exec "$@"