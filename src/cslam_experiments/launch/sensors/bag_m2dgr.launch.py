import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.actions import SetParameter


def launch_setup(context, *args, **kwargs):

    return [
        DeclareLaunchArgument('bag_file', default_value='', description=''),
        DeclareLaunchArgument('namespace', default_value='/r0',
                              description=''),
        DeclareLaunchArgument('rate', default_value='1.0', description=''),
        DeclareLaunchArgument('bag_start_delay',
                              default_value='5.0',
                              description=''),
        TimerAction(
            period=LaunchConfiguration('bag_start_delay'),
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'bag', 'play',
                        LaunchConfiguration('bag_file').perform(context), '-r',
                        LaunchConfiguration('rate'), '--remap',
                        '/velodyne_points:=' + LaunchConfiguration('namespace').perform(context) +
                        '/pointcloud',
                        '/ublox/fix:=' +
                        LaunchConfiguration('namespace').perform(context) +
                        '/gps/fix',
                        '/handsfree/imu:=' +
                        LaunchConfiguration('namespace').perform(context) +
                        '/imu/data'
                    ],
                    name='bag',
                    output='screen',
                )
            ]),
    ]


def generate_launch_description():

    return LaunchDescription([OpaqueFunction(function=launch_setup)])
