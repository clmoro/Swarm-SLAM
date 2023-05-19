import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    loop_detection_node = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace'))

    pose_graph_manager_node = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace'))

    return [
        loop_detection_node,
        pose_graph_manager_node,
    ]


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('namespace', default_value='/r5',
                              description=''),
        DeclareLaunchArgument('robot_id', default_value='5', description=''),
        DeclareLaunchArgument('max_nb_robots', default_value='8', description=''),
        DeclareLaunchArgument('config_path',
                              default_value=os.path.join(
                                  get_package_share_directory('cslam_experiments'),
                                  'config/'),
                              description=''),
        DeclareLaunchArgument('config_file',
                              default_value='blockchain.yaml',
                              description=''),
        DeclareLaunchArgument('config',
                              default_value=[
                                  LaunchConfiguration('config_path'),
                                  LaunchConfiguration('config_file')
                              ],
                              description=''),
        DeclareLaunchArgument(
            'launch_prefix_cslam',
            default_value='',
            description=
            'For debugging purpose, it fills prefix tag of the nodes, e.g., "xterm -e gdb -ex run --args"'
        ),
        DeclareLaunchArgument('enable_simulated_rendezvous',
                              default_value='false',
                              description=''),
        DeclareLaunchArgument('rendezvous_schedule_file',
                              default_value='',
                              description=''),
        DeclareLaunchArgument('log_level',
                              default_value='fatal',
                              description=''),
        OpaqueFunction(function=launch_setup),
    ])
