from rozum.rest import Robot
from rozum.rest.client.models import Position, Point, Rotation, Pose
import math
import random
import time
import logging
import numpy as np

logging.basicConfig(filename="nuts-app.log", level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

robot = Robot("192.168.0.150:8081")
nut_height = 0.024
nut_num = 6
n_places = nut_num + 1
cycles = 1
replaces = 6
z_offset = 0.13
aiming_offset = 0.06
SPEED = 150
REPETITIONS = 1000

class Nut(object):
    id = 0
    def __init__(self, aim_position, take_position):
        self.aim_position = aim_position
        self.take_position = take_position
        self.id = Nut.id % nut_num
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


def lin_interp(pos1:Position, pos2:Position, step=0.25):
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


def set_await(p):
    robot.set_position(p, speed=SPEED)
    robot.await_motion(0.05)


def run_await(p):
    robot.run_positions(p, speed=SPEED)
    robot.await_motion(0.05)


def move_nut(n: Nut, target_aim, target_take):
    logging.debug("Taking nut {} from {}".format(n.id, n.take_position))
    move_start = time.time()
    robot.close_gripper()
    run_await([n.aim_position, mid_position(n.aim_position, n.take_position), n.take_position])
    robot.open_gripper()
    logging.debug("Moving nut {} to {}".format(n.id, target_take))
    run_await([n.aim_position, target_aim, mid_position(target_aim, target_take), target_take])
    robot.close_gripper()
    set_await(target_aim)
    move_end = time.time()
    logging.debug("Moving from {} to {} took {} seconds".format(n.take_position, target_take, move_end - move_start))
    n.aim_position, n.take_position = target_aim, target_take

def move_nut_interp(n: Nut, target_aim, target_take):
    logging.debug("Taking nut {} from {}".format(n.id, n.take_position))
    move_start = time.time()
    run_await(lin_interp(n.aim_position, n.take_position))
    robot.open_gripper()
    logging.debug("Moving nut {} to {}".format(n.id, target_take))
    run_await([n.aim_position, *lin_interp(target_aim, target_take)])
    robot.close_gripper()
    run_await(lin_interp(target_take, target_aim))
    move_end = time.time()
    logging.debug("Moving from {} to {} took {} seconds".format(n.take_position, target_take, move_end - move_start))
    n.aim_position, n.take_position = target_aim, target_take

if __name__ == '__main__':
    targets1 = generate_target_coordinates(0.1, 0.43, 0.1)
    targets2 = generate_target_coordinates(0.6, 0.1, 0.1)
    start_point1 = (0.4, 0.45)
    start_point2 = (0.4, 0.3)
    center_aim1 = position_aim(0.1, 0.43, 0)
    center_aim2 = position_aim(0.6, 0.1, 0)
    start_time = time.time()
    for r in range(REPETITIONS):
        pack_positions_aim = packing_positions_aim(*start_point1, 3) + packing_positions_aim(*start_point2, 3)
        pack_positions_take = packing_positions_take(*start_point1, 3) + packing_positions_take(*start_point2, 3)
        unpack_positions_aim, unpack_positions_take = pack_positions_aim[::-1], pack_positions_take[::-1]

        aim_positions1, take_positions1 = aiming_positions(targets1), taking_positions(targets1)
        aim_positions2, take_positions2 = aiming_positions(targets2), taking_positions(targets2)

        nuts = list(map(lambda x: Nut(x[0], x[1]), zip(unpack_positions_aim, unpack_positions_take)))
        # unpack
        set_await(nuts[0].aim_position)
        time.sleep(5)
        robot.close_gripper()
        repetition_start = time.time()
        for n, aim, place in zip(nuts, aim_positions1, take_positions1):
            move_nut_interp(n, aim, place)

        # replaces
        for c in range(cycles):
            replace_cycle_start = time.time()
            for n, aim, place in zip(nuts, aim_positions2, take_positions2):
                move_nut_interp(n, aim, place)

            # for n, aim, place in zip(nuts, aim_positions1, take_positions1):
            #     move_nut(n, aim, place)
            replace_cycle_finish = time.time()
            logging.info("Replacing cycle {} time {} s".format(c, replace_cycle_finish - replace_cycle_start))

        # pack
        for n, pa, pt in zip(nuts, pack_positions_aim, pack_positions_take):
            move_nut(n, pa, pt)
        repetition_finish = time.time()
        logging.info("Repetition {} time {} s".format(r, repetition_finish - repetition_start))
    end_time = time.time()
    logging.info("Time elapsed from program start {} s".format(end_time - start_time))


