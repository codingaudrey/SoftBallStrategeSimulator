from projectile_simulator import ProjectileSimulator
from constants import DEFAULT_INTERVAL_MS
from src.coordinates import CartesianCoordinate
from id import ID
from math import pi


class BallInPlay:
    def __init__(self, exit_velocity: int, theta_vert: int, theta_hor: int, starting_height: float,
                 vacuum=True, interval=DEFAULT_INTERVAL_MS):
        self.v0 = exit_velocity
        self.tv = theta_vert
        self.th = theta_hor
        self.z0 = starting_height
        self.foul = False if -pi/4 < self.th < pi/4 else True
        self.path = self.path_3d(interval, vacuum)
        self.caught = None
        self.id = ID()

    def path_3d(self, interval=DEFAULT_INTERVAL_MS, vacuum=True) -> list[CartesianCoordinate]:
        if self.path:
            return self.path
        self.path = ProjectileSimulator.flight_path_3d_vacuum(self.tv, self.th, self.v0, self.z0, interval) \
            if vacuum \
            else ProjectileSimulator.flight_path_3d_air(self.tv, self.th, self.v0, self.z0, interval)
        return self.path

    def __repr__(self):
        return f"ID: {self.id}", f"Path: {self.path}"
