from routing import generate_route
from runner import Runner
import time

import numpy
from gpsapi import GpsApi
import gps_utils
import numpy as np

route = [
    [116.35091, 39.986832],
    [116.351836, 39.986842],
    [116.353156, 39.986891],
    [116.354225, 39.986946],
    [116.354513, 39.986946],
    [116.354638, 39.986932],
    [116.354629, 39.986808],
    [116.354638, 39.986725],
    [116.354656, 39.986358],
    [116.354629, 39.986096],
    [116.354674, 39.985453],
    [116.35471, 39.985253],
    [116.354719, 39.985073],
    [116.354845, 39.985032],
    [116.35515, 39.985052],
    [116.356067, 39.985045],
    [116.356713, 39.985059],
    [116.356848, 39.985094],
    [116.356848, 39.985253],
    [116.356839, 39.98537],
    [116.356821, 39.985564],
    [116.356803, 39.98594],
    [116.356794, 39.986428],
    [116.356767, 39.986777],
    [116.35674, 39.987008],
    [116.356839, 39.98706],
    [116.357032, 39.98706],
    [116.358312, 39.987098],
    [116.359557, 39.98716],
]

route = [gps_utils.bd09_to_wgs84(*p) for p in route]
route = list(route)

route = numpy.array(route)


gps = GpsApi('C:/yeshen/Nox/bin/nox_adb.exe')
gps.start_service()

route = generate_route(route)

runner = Runner(route, 1000/(2*60))  # 2min/km

time_start = time.time()

while True:
    t = time.time()-time_start
    pos = runner.calc_position_by_time(t)
    print(pos)

    gps.set_position(pos)

    # time.sleep(1.0)
    time.sleep(0.3)
