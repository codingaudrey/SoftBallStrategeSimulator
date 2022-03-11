from id import ID
from radius_manager import RadiusManager
from src.coordinates import PolarCoordinate, CartesianCoordinate
from constants import DEFAULT_INTERVAL_MS


class Fielder:
    def __init__(self, coordinates, polar=True, name=None, radius_manager=None):
        self.coordinates_cartesian = coordinates if not polar else self.polar_to_cartesian(coordinates)
        # self.coordinates_polar = coordinates if polar else self.polar_to_cartesian(coordinates)
        self.name = ID(name) if name else ID()
        self.radius_manager = radius_manager if radius_manager else RadiusManager()

    @staticmethod
    def polar_to_cartesian(polar_coord: PolarCoordinate) -> CartesianCoordinate:
        return polar_coord.cartesian_xy()

    @staticmethod
    def cartesian_to_polar(cartesian_coord: CartesianCoordinate) -> PolarCoordinate:
        return cartesian_coord.polar()

    def get_radius(self, time: float):
        return self.radius_manager.get_radius(time)

    def get_radii(self, total_time=10000, interval=DEFAULT_INTERVAL_MS):
        return self.radius_manager.get_radii(total_time, interval)

    def __repr__(self):
        return_string = ""
        return_string += f"name: {self.name}\n"
        return_string += self.coordinates_cartesian
        # return_string += self.coordinates_polar
        return_string += self.radius_manager
        return return_string
