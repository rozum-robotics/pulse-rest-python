from __future__ import absolute_import

import time

from pulserest.client import RobotApi
from pulserest.client.models import MotionStatus, MotionType, Pose, Position, Point, Rotation, Tool, Signal

__all__ = ['SIG_HIGH', 'SIG_LOW', 'MT_JOINT', 'MT_LINEAR', 'MotionStatus', 'position', 'pose', 'tool', 'RobotPulse']

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

    :param point: tuple or list containing x, y, z coordinates (in meters) where robot should move its TCP
    :param rotation: tuple or list containing roll, pitch, yaw coordinates (in radians) for TCP
    :return: Position
    """
    return Position(Point(*point), Rotation(*rotation))


def pose(angles):
    """Creates pose motion target.

    Use this method to create poses which will be passed to set_pose and run_poses methods of RobotPulse.

    :param angles: list containing 6 angles for motors (in degrees). Order: base-0th, tcp-6th
    :return: Pose
    """
    return Pose(angles)


def tool(tcp_position, radius, name='Unnamed'):
    return Tool(name=name, point=tcp_position.point, rotation=tcp_position.rotation, radius=radius)


class RobotPulse(object):
    def __init__(self, host=None):
        self._api = RobotApi()
        if host is not None:
            self._api.api_client.configuration.host = host

    def change_base(self, position):
        return self._api.change_base(position)

    def change_tool(self, tool):
        return self._api.change_tool(tool)

    def close_gripper(self, timeout=None):
        if timeout is not None:
            return self._api.close_gripper(timeout=timeout)
        return self._api.close_gripper()

    def freeze(self):
        return self._api.freeze()

    def get_base(self):
        return self._api.get_base()

    def get_digital_input(self, port):
        return self._api.get_digital_input(port)

    def get_digital_output(self, port):
        return self._api.get_digital_output(port)

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

    def run_poses(self, poses, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.run_poses(poses, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def run_positions(self, positions, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.run_positions(positions, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def set_digital_output_high(self, port):
        return self._api.set_digital_output_high(port)

    def set_digital_output_low(self, port):
        return self._api.set_digital_output_low(port)

    def set_pose(self, pose, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.set_pose(pose, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def set_position(self, position, speed, motion_type=MotionType.JOINT, tcp_max_velocity=2.0):
        return self._api.set_position(position, speed=speed, type=motion_type, tcp_max_velocity=tcp_max_velocity)

    def status_motion(self):
        return self._api.status_motion()

    def status_motors(self):
        return self._api.status_motors()

    def await_motion(self, asking_interval=0.1):
        while self.status_motion() != MotionStatus.IDLE:
            time.sleep(asking_interval)
