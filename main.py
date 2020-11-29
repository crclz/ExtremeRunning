import time

import numpy

import config
import gps_utils
from gpsapi import GpsApi
from routing import generate_route
from runner import Runner
import sys

# load route from file
if len(sys.argv) <= 1:
    print("请传递路径文件的命令行参数")
    print("示例: python main.py route-playground.txt")
    exit(-1)

route_file = sys.argv[1]
route = config.load_route_file(route_file)

# convert route from baidu format to wgs84
route = list([gps_utils.bd09_to_wgs84(*p) for p in route])

route = numpy.array(route)

# convert original route to smooth and long (100km) route
route = generate_route(route)

runner = Runner(route, 1000/(2*60))  # 2min/km

# start api service
gps = GpsApi('C:/yeshen/Nox/bin/nox_adb.exe')
gps.start_service()


# run:

time_start = time.time()

while True:
    t = time.time() - time_start
    pos = runner.calc_position_by_time(t)
    print(pos)

    gps.set_position(pos)

    # time.sleep(1.0)
    time.sleep(0.3)
