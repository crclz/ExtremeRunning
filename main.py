import time
from gpsapi import GpsApi
import gps_utils

gps = GpsApi('C:/yeshen/Nox/bin/nox_adb.exe')

gps.start_service()

run_path = [
    (116.352109, 39.986355),
    (116.352168, 39.985415),
    (116.352963, 39.98545),
    (116.352963, 39.98545)
]

run_path = [gps_utils.gcj02_to_wgs84(*p) for p in run_path]
run_path = list(run_path)

plan_sec = 10
interval = 0.2

pos = run_path[0]

i = 0
while True:
    p1 = run_path[i % len(run_path)]
    p2 = run_path[(i+1) % len(run_path)]

    steps = int(plan_sec/interval)

    dx = p2[0]-p1[0]
    dx /= steps
    dy = p2[1]-p1[1]
    dy /= steps

    for t in range(steps):
        x = pos[0]+dx
        y = pos[1]+dy
        pos = (x, y)
        gps.set_position(pos)
        time.sleep(interval)

    i += 1
