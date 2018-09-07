from __future__ import absolute_import
from rozum.rest.client import RobotApi
from rozum.rest.client.models import MotionStatus, MotionType
import time


class Robot(object):
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

    def run_poses(self, poses, speed, type=MotionType.JOINT):
        return self._api.run_poses(poses, speed=speed, type=type)

    def run_positions(self, positions, speed, type=MotionType.JOINT):
        return self._api.run_positions(positions, speed=speed, type=type)

    def set_digital_output_high(self, port):
        return self._api.set_digital_output_high(port)

    def set_digital_output_low(self, port):
        return self._api.set_digital_output_low(port)

    def set_pose(self, pose, speed, type=MotionType.JOINT):
        return self._api.set_pose(pose, speed=speed, type=type)

    def set_position(self, position, speed, type=MotionType.JOINT):
        return self._api.set_position(position, speed=speed, type=type)

    def status_motion(self):
        return self._api.status_motion()

    def status_motors(self):
        return self._api.status_motors()

    def await_motion(self, asking_interval=0.1):
        while self.status_motion() != MotionStatus.IDLE:
            time.sleep(asking_interval)
