import gps_utils
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

run_path = [
    (116.35206, 39.986348),
    (116.352118, 39.986148),
    (116.352145, 39.985626),
    (116.352154, 39.985433),
    (116.352199, 39.985243),
    (116.352617, 39.985101),
    (116.352868, 39.985198),
    (116.353012, 39.985443),
    (116.352994, 39.985595),
    (116.352963, 39.985806),
    (116.352981, 39.985899),
    (116.352927, 39.986272),
]

run_path = [gps_utils.bd09_to_wgs84(*p) for p in run_path]
run_path = list(run_path)

points = np.array(run_path)

distance = np.cumsum(np.sqrt(np.sum(np.diff(points, axis=0)**2, axis=1)))
distance = np.insert(distance, 0, 0)/distance[-1]


# Interpolation for different methods:
interpolations_methods = ['slinear', 'quadratic', 'cubic']
alpha = np.linspace(0, 1, 75)

interpolated_points = {}
for method in interpolations_methods:
    interpolator = interp1d(distance, points, kind=method, axis=0)
    interpolated_points[method] = interpolator(alpha)

# Graph:
plt.figure(figsize=(7, 7))
for method_name, curve in interpolated_points.items():
    plt.plot(*curve.T, '-', label=method_name)

plt.plot(*points.T, 'ok', label='original points')
plt.axis('equal')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.show()
