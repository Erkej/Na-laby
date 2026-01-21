#!/bin/bash
set -e
cd /ros2_ws
source /opt/ros/humble/setup.sh
mkdir /ros2_ws/src
cd /ros2_ws/src
ros2 pkg create ros_project --build-type ament_python --dependencies cv_bridge python3-opencv sensor_msgs geometry_msgs trajectory_msgs
cp /src/src/ros_project/robot_cont.py /ros2_ws/src/ros_project/ros_project/robot_cont.py
cp /src/src/ros_project/camera_subs.py /ros2_ws/src/ros_project/ros_project/camera_subs.py
mkdir /ros2_ws/src/ros_project/launch
cp /src/src/ros_project/launch/start.launch.py /ros2_ws/src/ros_project/launch/start.launch.py
cp /src/src/ros_project/setup.py  /ros2_ws/src/ros_project/setup.py

cd /ros2_ws
colcon build
source ./install/setup.sh
ros2 launch ur_robot_driver ur_control.launch.py \
    ur_type:=ur5 \
    robot_ip:=yyy.yyy.yyy.yyy \
    use_fake_hardware:=true \
    launch_rviz:=true \
    initial_joint_controller:=joint_trajectory_controller &
ros2 launch ros_project start.launch.py &

exec "$@"