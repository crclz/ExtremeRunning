from gpsapi import GpsApi
import gps_utils

gps = GpsApi('C:/yeshen/Nox/bin/nox_adb.exe')

gps.start_service()

pos = [116.34598005620576, 39.98017009264535]
pos = gps_utils.gcj02_to_wgs84(*pos)

o2 = gps.set_latitude(pos[1])

o2 = gps.set_longitude(pos[0])
