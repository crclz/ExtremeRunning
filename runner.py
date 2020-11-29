import route
import numpy as np


class Runner():

    # 累计的距离
    dist_list = None

    def __init__(self, route_points, velocity) -> None:
        """
        route_points -- numpy array of shape(n, 2), each row is [lon, lat]\n
        v -- velocity (m/s)
        """

        assert route_points.shape[1] == 2
        assert velocity > 0

        self.route = route_points
        self.velocity = velocity

        dist_list = route.route_dist_list(self.route)
        assert dist_list[0] == 0

        self.dist_list = np.cumsum(dist_list)

    def calc_position_by_distance(self, dist):
        assert dist > self.dist_list[0]
        assert dist < self.dist_list[-1]
        ix = np.searchsorted(self.dist_list, dist)
        return self.route[ix]

    def calc_position_by_time(self, t):
        dist = t * self.velocity
        return self.calc_position_by_distance(dist)


if __name__ == "__main__":
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
        [116.352056, 39.986403]
    ]

    run_path = np.array(run_path)

    rt = route.get_route(run_path, 10000)

    runner = Runner(run_path, 1000/(5*60))

    p = runner.calc_position_by_distance(400)

    print(p)
