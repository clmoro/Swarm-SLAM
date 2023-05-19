import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def launch_setup(context, *args, **kwargs):
    loop_detection_node_1 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_1'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_1'))

    pose_graph_manager_node_1 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_1'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_1'))

    loop_detection_node_2 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_2'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_2'))

    pose_graph_manager_node_2 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_2'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_2'))

    loop_detection_node_3 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_3'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_3'))

    pose_graph_manager_node_3 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_3'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_3'))

    loop_detection_node_4 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_4'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_4'))

    pose_graph_manager_node_4 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_4'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_4'))

    loop_detection_node_5 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_5'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_5'))

    pose_graph_manager_node_5 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_5'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_5'))

    loop_detection_node_6 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_6'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_6'))

    pose_graph_manager_node_6 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_6'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_6'))

    loop_detection_node_7 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_7'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_7'))

    pose_graph_manager_node_7 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_7'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_7'))

    loop_detection_node_8 = Node(package='cslam',
                               executable='loop_closure_detection_node.py',
                               name='cslam_loop_closure_detection',
                               parameters=[
                                   LaunchConfiguration('config'), {
                                       "robot_id":
                                       LaunchConfiguration('robot_id_8'),
                                       "max_nb_robots":
                                       LaunchConfiguration('max_nb_robots'),
                                   }
                               ],
                               namespace=LaunchConfiguration('namespace_8'))

    pose_graph_manager_node_8 = Node(package='cslam',
                                   executable='pose_graph_manager',
                                   name='cslam_pose_graph_manager',
                                   parameters=[
                                       LaunchConfiguration('config'), {
                                           "robot_id":
                                           LaunchConfiguration('robot_id_8'),
                                           "max_nb_robots":
                                           LaunchConfiguration('max_nb_robots'),
                                           "evaluation.enable_simulated_rendezvous": LaunchConfiguration('enable_simulated_rendezvous'),
                                           "evaluation.rendezvous_schedule_file": LaunchConfiguration('rendezvous_schedule_file'),
                                       }
                                   ],
                                   prefix=LaunchConfiguration('launch_prefix_cslam'),
                                   namespace=LaunchConfiguration('namespace_8'))                                                                                                                                                           

    return [
        loop_detection_node_1,
        pose_graph_manager_node_1,
        loop_detection_node_2,
        pose_graph_manager_node_2,
        loop_detection_node_3,
        pose_graph_manager_node_3,
        loop_detection_node_4,
        pose_graph_manager_node_4,
        loop_detection_node_5,
        pose_graph_manager_node_5,
        loop_detection_node_6,
        pose_graph_manager_node_6,
        loop_detection_node_7,
        pose_graph_manager_node_7,
        loop_detection_node_8,
        pose_graph_manager_node_8,
    ]


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('namespace_1', default_value='/r0',
                              description=''),
        DeclareLaunchArgument('robot_id_1', default_value='0', description=''),
        DeclareLaunchArgument('namespace_2', default_value='/r1',
                              description=''),
        DeclareLaunchArgument('robot_id_2', default_value='1', description=''),
        DeclareLaunchArgument('namespace_3', default_value='/r2',
                              description=''),
        DeclareLaunchArgument('robot_id_3', default_value='2', description=''),
        DeclareLaunchArgument('namespace_4', default_value='/r3',
                              description=''),
        DeclareLaunchArgument('robot_id_4', default_value='3', description=''),
        DeclareLaunchArgument('namespace_5', default_value='/r4',
                              description=''),
        DeclareLaunchArgument('robot_id_5', default_value='4', description=''),
        DeclareLaunchArgument('namespace_6', default_value='/r5',
                              description=''),
        DeclareLaunchArgument('robot_id_6', default_value='5', description=''),
        DeclareLaunchArgument('namespace_7', default_value='/r6',
                              description=''),
        DeclareLaunchArgument('robot_id_7', default_value='6', description=''),
        DeclareLaunchArgument('namespace_8', default_value='/r7',
                              description=''),
        DeclareLaunchArgument('robot_id_8', default_value='7', description=''),
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
