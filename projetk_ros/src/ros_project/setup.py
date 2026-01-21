from setuptools import find_packages, setup
import os              
from glob import glob

package_name = 'ros_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vin',
    maintainer_email='root@todo.todo',
    description='Ros2 project',
    license='BSD-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_cont = ros_project.robot_cont:main',
            'camera_subs = ros_project.camera_subs:main'
        ],
    },
)