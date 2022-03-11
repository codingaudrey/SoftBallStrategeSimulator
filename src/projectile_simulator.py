from src.coordinates import CartesianCoordinate
import numpy as np


GRAVITY = -9.8
FEET = 3.28


class ProjectileSimulator:
    def __init__(self, v0: int, theta_horizontal: int, theta_vertical: int):
        pass

    @staticmethod
    def flight_path_2d_vacuum(vert_angle: float, exit_velo: float,
                              starting_height: float, interval_ms: float, imperial=False) -> list[CartesianCoordinate]:
        vx0 = exit_velo * np.cos(vert_angle)
        vy0 = exit_velo * np.sin(vert_angle)
        y0 = starting_height
        time_s = 0
        time_ms = 0
        flightpath = [CartesianCoordinate(0, starting_height)]
        while flightpath[-1].y >= 0:
            time_ms += interval_ms
            time_s = time_ms / 1000
            next_x = vx0 * time_s
            next_y = (y0 + vy0 * time_s + GRAVITY/2*time_s**2)
            if imperial:
                flightpath.append(CartesianCoordinate(next_x * FEET, next_y * FEET))
            else:
                flightpath.append(CartesianCoordinate(next_x, next_y))
        return flightpath

    @staticmethod
    def flight_path_2d_air(vert_angle: float, exit_velo: float,
                           starting_height: float, interval_ms: float) -> list[CartesianCoordinate]:
        pass

    @staticmethod
    def flight_path_3d_vacuum(vert_angle: float, horiz_angle: float, exit_velo: float,
                              starting_height: float, interval_ms: float) -> list[CartesianCoordinate]:
        flight_path_2d = ProjectileSimulator.flight_path_2d_vacuum(vert_angle, exit_velo, starting_height, interval_ms)
        return ProjectileSimulator.flight_path_2d_to_3d(flight_path_2d, horiz_angle)

    @staticmethod
    def flight_path_3d_air(vert_angle: float, horiz_angle: float, exit_velo: float,
                           starting_height: float, interval_ms: float) -> list[CartesianCoordinate]:
        pass

    @staticmethod
    def flight_path_2d_to_3d(path_2d: list[CartesianCoordinate], horiz_angle: float) -> list[CartesianCoordinate]:
        path = []
        for coord in path_2d:
            path.append(CartesianCoordinate(coord.x * np.cos(horiz_angle), coord.x * np.sin(horiz_angle), coord.y))
        return path

