import math

import numpy
import gps_utils
import numpy as np
from scipy.interpolate import interp1d

run_path = [
    [116.35206, 39.986348],
    [116.352118, 39.986148],
    [116.352145, 39.985626],
    [116.352154, 39.985433],
    [116.352199, 39.985243],
    [116.352617, 39.985101],
    [116.352868, 39.985198],
    [116.353012, 39.985443],
    [116.352994, 39.985595],
    [116.352963, 39.985806],
    [116.352981, 39.985899],
    [116.352927, 39.986272],
    [116.352914, 39.986524],
    [116.352779, 39.986624],
    [116.352433, 39.986725],
    [116.352433, 39.986725],
    [116.352056, 39.986403]
]


def get_smooth_route(route, segments):
    points = np.array(route)

    distance = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1)))
    distance = np.insert(distance, 0, 0)/distance[-1]

    # Interpolation for different methods:
    alpha = np.linspace(0, 1, segments)

    interpolator = interp1d(distance, points, kind='cubic', axis=0)
    route = interpolator(alpha)
    return route


def route_dist_list(route):
    r1 = route[:-1]
    r2 = route[1:]
    lon1 = r1[:, 0]
    lat1 = r1[:, 1]
    lon2 = r2[:, 0]
    lat2 = r2[:, 1]
    dist_list = gps_utils.distance(lon1, lat1, lon2, lat2)
    dist_list = np.insert(dist_list, 0, 0)
    return dist_list


def repeat_route(route, tot_dist):
    """
    route -- numpy array of shape (n, 2)\n
    tot_dist -- repeat route to tot_dist (meters)\n
    """

    assert route.shape[1] == 2

    dist_list = route_dist_list(route)
    dist = dist_list.sum()

    repeat_times = math.ceil(tot_dist/dist)

    repeated = []
    for i in range(repeat_times):
        repeated.append(route)

    repeated = np.concatenate(repeated)

    assert repeated.shape[1] == 2

    return repeated


def generate_route(route):
    """
    route -- numpy array of shape (n, 2)\n
    """
    assert route.shape[1] == 2

    tot_dist = 100*1000  # 100km
    segments = tot_dist * 2  # 2 segments per meter

    route = repeat_route(route, tot_dist)

    # smoothing the route
    route = get_smooth_route(route, segments)

    return route
