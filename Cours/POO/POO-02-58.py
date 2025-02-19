from dataclasses import astuple
from point3 import ThreeDPoint

point_1 = ThreeDPoint(1.0, 2.0, 3.0)
print(point_1)
print(astuple(point_1))
point_2 = ThreeDPoint(2, 3, 4)
print(point_1 == point_2)
point_3 = ThreeDPoint(1, 2, 3)
print(point_1 == point_3)