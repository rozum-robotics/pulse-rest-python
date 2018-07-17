from rozum.rest import Robot
from rozum.rest.client.models import Position, Point, Rotation, Pose
import math
import random
import time
import logging
import numpy as np
from collections import deque
# import pandas as pd

logging.basicConfig(filename="nuts-app.log", level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
logging.getLogger("rozum.rest.client.rest").setLevel(logging.WARNING)

robot = Robot("192.168.0.150:8081")
nut_height = 0.024
nut_num = 6
n_places = nut_num + 1
cycles = 1
replaces = 6
z_offset = 0.138
aiming_offset = 0.06
SPEED = 100
REPETITIONS = 1000
data = {"x":[], "y":[], "z":[]}

def update_data(p: Position):
    data["x"].append(p.point.x)
    data["y"].append(p.point.y)
    data["z"].append(p.point.z)

class Nut(object):
    id = 0

    def __init__(self, aim_position, take_position):
        self.aim_position = aim_position
        self.take_position = take_position
        self.id = Nut.id % nut_num
        self.next_nut = None
        Nut.id += 1


def generate_target_coordinates(x: float, y: float, r: float):
    start_angle, angle_delta = 0, 2 * math.pi / nut_num
    def get_next_point(i): return x + r * math.cos(start_angle + angle_delta * i), y + r * math.sin(start_angle + angle_delta * i)
    return [get_next_point(i) for i in range(nut_num)]


def position_vertical(x, y, z): return Position(Point(x, y, z), Rotation(math.pi, 0, 0))


def position_aim(x, y, z): return position_vertical(x, y, z + z_offset + aiming_offset)


def position_take(x, y, z): return position_vertical(x, y, z + z_offset)


def mid_position(p1:Position, p2:Position):
    return position_vertical((p1.point.x + p2.point.x) / 2, (p1.point.y + p2.point.y) / 2, (p1.point.z + p2.point.z) / 2)


def lin_interp(pos1:Position, pos2:Position, step=0.2):
    p1, p2 = pos1.point, pos2.point
    v1, v2 = np.array([p1.x, p1.y, p1.z]), np.array([p2.x, p2.y, p2.z])
    v = v2 - v1
    n = 1 / step
    return list(map(lambda i: position_vertical(*(v1 + v * i).data), np.linspace(0., 1., int(n))))


def aiming_positions(coordinates: list):
    return [position_aim(v[0], v[1], 0) for v in coordinates]


def taking_positions(coordinates: list):
    return [position_take(v[0], v[1], 0) for v in coordinates]


def packing_positions_aim(x, y, num): return list(map(lambda i: position_aim(x, y, i * nut_height), range(num)))


def packing_positions_take(x, y, num): return list(map(lambda i: position_take(x, y, i * nut_height), range(num)))


def smoothing_position(pos1: Position, pos2: Position, delta=0.5):
    p1, p2 = pos1.point, pos2.point
    v1, v2 = np.array([p1.x, p1.y, p1.z]), np.array([p2.x, p2.y, p2.z])
    v = v2 - v1
    v[2] *= -1
    return position_vertical(*(v1 + v*delta).data)


def set_await(p):
    robot.set_position(p, speed=SPEED)
    robot.await_motion(0.05)


def run_await(p):
    robot.run_positions(p, speed=SPEED)
    robot.await_motion(0.05)


def move_nut_interp(n: Nut, target_aim, target_take):
    logging.debug("Taking nut {} from {}".format(n.id, n.take_position))
    move_start = time.time()
    positions_before_take = lin_interp(n.aim_position, n.take_position)
    run_await(positions_before_take)
    list(map(update_data, positions_before_take))
    robot.open_gripper(100)
    logging.debug("Moving nut {} to {}".format(n.id, target_take))
    replacing_positions = [n.aim_position, *lin_interp(target_aim, target_take)]
    run_await(replacing_positions)
    list(map(update_data, replacing_positions))
    robot.close_gripper(50)
    go_up = lin_interp(target_take, target_aim)[1:]
    after_replacing_positions = [*go_up, ]
    run_await(after_replacing_positions)
    list(map(update_data, after_replacing_positions))
    move_end = time.time()
    logging.debug("Moving from {} to {} took {} seconds".format(n.take_position, target_take, move_end - move_start))
    n.aim_position, n.take_position = target_aim, target_take


def operation_cycle(nuts_list, aims_list, takes_list):
    zipped = zip(nuts_list, aims_list, takes_list)
    for n, aim, take in zipped:
        if n.id == 0:
            robot.close_gripper(50)
            first_positions = lin_interp(n.aim_position, n.take_position)
            run_await(first_positions)
            list(map(update_data, first_positions))
        robot.open_gripper(100)
        l1, l2 = lin_interp(n.take_position, n.aim_position)[1:], lin_interp(aim, take)
        lin_mid = lin_interp(l1[-1], l2[0], 0.25)[:-1]
        mid_positions = l1 + l2
        run_await(mid_positions)
        list(map(update_data, mid_positions))
        robot.close_gripper(50)
        last_positions = lin_interp(take, aim)[1:]
        if n.id != 5:
            position___ = lin_interp(last_positions[-1], n.next_nut.aim_position, 0.2)[1:-1]
            last_positions += lin_interp(n.next_nut.aim_position, n.next_nut.take_position)
            run_await(last_positions)
        else:
            run_await(last_positions)
        list(map(update_data, last_positions))
        n.take_position, n.aim_position = take, aim


if __name__ == '__main__':
    c1, c2 = (-0.6, -0.1), (-0.1, -0.6)
    targets1 = generate_target_coordinates(*c1, 0.1)
    targets2 = generate_target_coordinates(*c2, 0.1)
    start_point1 = (-0.35, -0.35)
    start_point2 = (-0.3, -0.3)
    start_time = time.time()
    for r in range(REPETITIONS):
        pack_positions_aim = packing_positions_aim(*start_point1, 3) + packing_positions_aim(*start_point2, 3)
        pack_positions_take = packing_positions_take(*start_point1, 3) + packing_positions_take(*start_point2, 3)
        unpack_positions_aim, unpack_positions_take = pack_positions_aim[::-1], pack_positions_take[::-1]

        aim_positions1, take_positions1 = aiming_positions(targets1), taking_positions(targets1)
        aim_positions2, take_positions2 = aiming_positions(targets2), taking_positions(targets2)

        nuts = list(map(lambda x: Nut(x[0], x[1]), zip(unpack_positions_aim, unpack_positions_take)))
        shifted_nuts = deque(nuts)
        shifted_nuts.rotate(-1)
        def add_next_nut(x):
            x[0].next_nut = x[1]
        list(map(add_next_nut, zip(nuts, shifted_nuts)))
        # unpack
        set_await(nuts[0].aim_position)
        time.sleep(5)
        robot.close_gripper(100)
        repetition_start = time.time()
        # first nut
        unpack = list(zip(nuts, aim_positions1, take_positions1))

        operation_cycle(nuts, aim_positions1, take_positions1)

        # replaces
        for c in range(cycles):
            replace_cycle_start = time.time()
            operation_cycle(nuts, aim_positions2, take_positions2)
            # operation_cycle(nuts, aim_positions1, take_positions1)
            replace_cycle_finish = time.time()
            logging.info("Replacing cycle {} time {} s".format(c, replace_cycle_finish - replace_cycle_start))

        # pack
        operation_cycle(nuts, pack_positions_aim, pack_positions_take)
        # pd.DataFrame(data).to_csv("movements.csv")
        repetition_finish = time.time()
        logging.info("Repetition {} time {} s".format(r, repetition_finish - repetition_start))
    end_time = time.time()
    logging.info("Time elapsed from program start {} s".format(end_time - start_time))


