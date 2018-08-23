from rozum.rest.client import RobotApi
from rozum.rest.client.models import MotionStatus
import time


class Robot(object):
    def __init__(self, host=None):
        self.api = RobotApi()
        if host is not None:
            self.api.api_client.configuration.host = host

    def change_base(self, position):
        return self.api.change_base(position)

    def change_tool(self, tool):
        return self.api.change_tool(tool)

    def close_gripper(self, timeout=None):
        if timeout is not None:
            return self.api.close_gripper(timeout=timeout)
        return self.api.close_gripper()

    def get_position(self):
        return self.api.get_position()

    def set_position(self, position, speed):
        return self.api.set_position(position, speed=speed)

    def run_positions(self, positions, speed):
        return self.api.run_positions(positions, speed=speed)

    def get_pose(self):
        return self.api.get_pose()

    def set_pose(self, pose, speed):
        return self.api.set_pose(pose, speed=speed)

    def run_poses(self, poses, speed):
        return self.api.run_poses(poses, speed=speed)

    def open_gripper(self, timeout=None):
        if timeout is not None:
            return self.api.open_gripper(timeout=timeout)
        return self.api.open_gripper()

    def relax(self):
        return self.api.relax()

    def freeze(self):
        return self.api.freeze()

    def status_motion(self):
        return self.api.status_motion()

    def await_motion(self, asking_interval=0.1):
        while self.status_motion() != MotionStatus.IDLE:
            time.sleep(asking_interval)

    def status_motion(self):
        return self.api.status_motion()

    def status_motors(self):
        return self.api.status_motors()
