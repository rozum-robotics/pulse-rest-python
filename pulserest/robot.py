from __future__ import absolute_import

import time

from pulserest.client import RobotApi
from pulserest.client.models import (MotionStatus,
                                     MotionType,
                                     Pose,
                                     Position,
                                     Point,
                                     Rotation,
                                     Tool,
                                     Signal,
                                     BoxObstacle,
                                     CapsuleObstacle,
                                     PlaneObstacle)

__all__ = ['SIG_HIGH', 'SIG_LOW', 'MT_JOINT', 'MT_LINEAR', 'MotionStatus', 'Point', 'Rotation',
           'position', 'pose', 'tool', 'RobotPulse',
           'create_box_obstacle', 'create_capsule_obstacle', 'create_plane_obstacle']

SIG_HIGH = Signal.HIGH
SIG_LOW = Signal.LOW
MT_JOINT = MotionType.JOINT
MT_LINEAR = MotionType.LINEAR


def position(point, rotation):
    """Creates position motion target.

    Use this method to create positions which will be passed to set_position and run_positions methods of RobotPulse.

    Example: there is need to move robot's TCP to point with coordinates x=0.3m, y=0.2m, z=0.1m
    and look down vertically relative to base. Call _position((0.3, 0.2, 0.1), (3.1415, 0, 0))_ and pass result to one
    of the methods mentioned earlier.

    :param point: list containing x, y, z coordinates (in meters) where robot should move its TCP
    :param rotation: list containing roll, pitch, yaw coordinates (in radians) for TCP
    :return: Position
    """
    return Position(Point(*point), Rotation(*rotation))


def pose(angles):
    """Creates pose motion target.

    Use this method to create poses which will be passed to set_pose and run_poses methods of RobotPulse.

    :param angles: list containing 6 angles for motors (in degrees). Order: base-0th, tcp-5th
    :return: Pose
    """
    return Pose(angles)


def tool(tcp_position, shape, name='unnamed_tool'):
    return Tool(name=name, tcp=tcp_position, shape=shape)


def create_box_obstacle(sides, center_position, name='unnamed_box'):
    return BoxObstacle('BOX', name, sides, center_position)


def create_capsule_obstacle(radius, start_point, end_point, name='unnamed_capsule'):
    return CapsuleObstacle('CAPSULE', name,  radius, start_point, end_point)


def create_plane_obstacle(points, name='unnamed_plane'):
    return PlaneObstacle('PLANE', name, points)


class RobotPulse(object):
    def __init__(self, host=None):
        self._api = RobotApi()
        if host is not None:
            self._api.api_client.configuration.host = host

    def add_to_environment(self, obstacle):
        return self._api.add_to_environment(obstacle)

    def change_base(self, base_position):
        return self._api.change_base(base_position)

    def change_tool(self, new_tool):
        return self._api.change_tool(new_tool)

    def close_gripper(self, timeout=None):
        if timeout is not None:
            return self._api.close_gripper(timeout=timeout)
        return self._api.close_gripper()

    def freeze(self):
        return self._api.freeze()

    def get_all_from_environment(self):
        return self._api.get_all_from_environment()

    def get_base(self):
        return self._api.get_base()

    def get_digital_input(self, port):
        return self._api.get_digital_input(port)

    def get_digital_output(self, port):
        return self._api.get_digital_output(port)

    def get_from_environment_by_name(self, obstacle_name):
        return self._api.get_from_environment_by_name(obstacle_name)

    def get_pose(self):
        return self._api.get_pose()

    def get_position(self):
        return self._api.get_position()

    def get_tool(self):
        return self._api.get_tool()

    def identifier(self):
        return self._api.identifier()

    def open_gripper(self, timeout=None):
        if timeout is not None:
            return self._api.open_gripper(timeout=timeout)
        return self._api.open_gripper()

    def pack(self):
        return self._api.pack()

    def recover(self):
        return self._api.recover()

    def relax(self):
        return self._api.relax()

    def remove_all_from_environment(self):
        return self._api.remove_all_from_environment()

    def remove_from_environment_by_name(self, obstacle_name):
        return self._api.remove_from_environment_by_name(obstacle_name)

    def run_poses(self, poses, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.run_poses(poses, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def run_positions(self, positions, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.run_positions(positions, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def set_digital_output_high(self, port):
        return self._api.set_digital_output_high(port)

    def set_digital_output_low(self, port):
        return self._api.set_digital_output_low(port)

    def set_pose(self, target_pose, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.set_pose(target_pose, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def set_position(self, target_position, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.set_position(target_position, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def status_motion(self):
        return self._api.status_motion()

    def status_motors(self):
        return self._api.status_motors()

    def await_motion(self, asking_interval=0.1):
        while self.status_motion() != MotionStatus.IDLE:
            time.sleep(asking_interval)
