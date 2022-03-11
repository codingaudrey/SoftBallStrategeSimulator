import math
from math import cos, sin, sqrt, atan
from random import Random


class PolarCoordinate:
    def __init__(self, radius: float, theta_horizontal: float, theta_vertical=0.0):
        self.radius = radius
        self.theta_vertical = theta_vertical
        self.theta_horizontal = theta_horizontal

    def cartesian(self):
        x = self.radius * cos(self.theta_horizontal) * cos(self.theta_vertical)
        y = self.radius * sin(self.theta_horizontal) * cos(self.theta_vertical)
        z = self.radius * sin(self.theta_vertical) * cos(self.theta_horizontal)
        return CartesianCoordinate(x, y, z)

    def cartesian_xy(self):
        x = self.radius * cos(self.theta_horizontal)
        y = self.radius * sin(self.theta_horizontal)
        return CartesianCoordinate(x, y)

    def __repr__(self):
        return f"(radius: {self.radius}, angle horizontal: {self.theta_horizontal}, angle vertical: {self.theta_vertical})\n"


class CartesianCoordinate:
    def __init__(self, x: float, y: float, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def polar(self) -> PolarCoordinate:
        r = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        if r == 0:
            return PolarCoordinate(0, 0, 0)
        if self.x == 0:
            theta_horizontal = 0 if self.y == 0 else math.pi/2 if self.y > 0 else -math.pi/2
            theta_vertical = 0 if self.z == 0 else math.pi/2 if self.z > 0 else -math.pi/2
        else:
            theta_horizontal = atan(self.y / self.x)
            theta_vertical = atan(self.z / self.x)

        return PolarCoordinate(r, theta_horizontal, theta_vertical)



    def __repr__(self):
        return f"(x: {self.x}, y: {self.y}, z: {self.z})\n"

    def __eq__(self, other):
        return (self.x - other.x) ** 2 < .001 and \
               (self.y - other.y) ** 2 < .001 and \
               (self.z - other.z) ** 2 < .001


if __name__ == '__main__':
    test_cases = []
    random = Random()
    for _ in range(10):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        z = random.randint(0, 10)
        test_cases.append(CartesianCoordinate(x, y, z))

    for cartesian_coord in test_cases:
        if cartesian_coord == cartesian_coord.polar().cartesian():
            print(f"pass: {cartesian_coord}")
        else:
            print(f"fail: {cartesian_coord}")
        print(cartesian_coord.polar())
        print(cartesian_coord.polar().cartesian())

