import os
import time

import numpy

import config
import gps_utils
from gpsapi import GpsApi
from routing import generate_route
from runner import Runner
import sys

# check nox adb path
with open("nox-path.txt", 'r', encoding='utf8') as f:
    nox_path = f.read()
    nox_path = nox_path.strip()
    nox_adb_path = nox_path + "/bin/nox_adb.exe"

if not os.path.exists(nox_adb_path):
    print(f"文件不存在: {nox_adb_path}")
    print("请正确修改 nox-path.txt 的内容")
    exit(-1)

# load route from file
if len(sys.argv) <= 1:
    print("请传递命令行参数: 路径文件")
    print("示例: python main.py route-playground.txt 3.33")
    exit(-1)

if len(sys.argv) <= 2:
    print("请传递命令行参数: 速度(m/s)")
    print("示例: python main.py route-playground.txt 3.33")
    exit(-1)

route_file = sys.argv[1]
route = config.load_route_file(route_file)

velocity = float(sys.argv[2])

print(f"路径: {route_file}")
print(f"速度: {velocity}")

# convert route from baidu format to wgs84
route = list([gps_utils.bd09_to_wgs84(*p) for p in route])

route = numpy.array(route)

# convert original route to smooth and long (100km) route
route = generate_route(route)

runner = Runner(route, velocity)  # 2min/km

# start api service
gps = GpsApi(nox_adb_path)
gps.start_service()


# run:

time_start = time.time()

print("Running ...")

while True:
    t = time.time() - time_start
    pos = runner.calc_position_by_time(t)
    # print(pos)

    gps.set_position(pos)

    # time.sleep(1.0)
    time.sleep(0.3)
