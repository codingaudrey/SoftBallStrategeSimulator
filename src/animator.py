import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, PathPatch
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import numpy as np
from catch_calculator import CatchCalculator
from coordinates import CartesianCoordinate
from lineup import LineUp
from constants import FIELD_RADIUS

METERS = 1/3.28

OUTFIELD_XY = (0, 0)
OUTFIELD_RADIUS = FIELD_RADIUS

FILLER_1_XY = (-20 * METERS, 0)
FILLER_1_WIDTH = -280 * METERS
FILLER_1_HEIGHT = 15 * METERS

FILLER_2_XY = (-20 * METERS, 0)
FILLER_2_WIDTH = 15 * METERS
FILLER_2_HEIGHT = -290 * METERS

HOME_PLATE_XY = (0, (0-1.4142) * METERS)
HOME_PLATE_WIDTH = 2 * METERS
HOME_PLATE_HEIGHT = 2 * METERS

FIRST_BASE_XY = (42.42 * METERS, (-42.42-1.4142) * METERS)
FIRST_BASE_WIDTH = 2 * METERS
FIRST_BASE_HEIGHT = 2 * METERS

SECOND_BASE_XY = (84.85 * METERS, (0-1.4142) * METERS)
SECOND_BASE_WIDTH = 2 * METERS
SECOND_BASE_HEIGHT = 2 * METERS

THIRD_BASE_XY = (42.42 * METERS, (42.42-1.4142) * METERS)
THIRD_BASE_WIDTH = 2 * METERS
THIRD_BASE_HEIGHT = 2 * METERS

PITCHERS_PLATE_XY = (50 * METERS, -2 * METERS)
PITCHERS_PLATE_WIDTH = .5 * METERS
PITCHERS_PLATE_HEIGHT = 4 * METERS

INFIELD_XY = (50 * METERS, 0)
INFIELD_RADIUS = 65 * METERS


class Animator:
    def __init__(self):
        pass

    @staticmethod
    def single_image(filename: str, lineup: LineUp, results: list[[bool, list[(str, CartesianCoordinate)], list[CartesianCoordinate]]]):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(projection='3d')

        outfield = Circle(OUTFIELD_XY, OUTFIELD_RADIUS, color="black", fill=False, alpha=1, zorder=1)
        ax.add_patch(outfield)
        art3d.pathpatch_2d_to_3d(outfield, z=0, zdir="z")

        infield = Circle(INFIELD_XY, INFIELD_RADIUS, color="tan", fill=False, alpha=.7, zorder=100)
        ax.add_patch(infield)
        art3d.pathpatch_2d_to_3d(infield, z=0, zdir="z")

        filler1 = Rectangle(FILLER_1_XY, FILLER_1_WIDTH, FILLER_1_HEIGHT, color="black", alpha=1, zorder=100, angle=135)
        ax.add_patch(filler1)
        art3d.pathpatch_2d_to_3d(filler1, z=1, zdir="z")

        filler2 = Rectangle(FILLER_2_XY, FILLER_2_WIDTH, FILLER_2_HEIGHT, color="black", alpha=1, zorder=101, angle=135)
        ax.add_patch(filler2)
        art3d.pathpatch_2d_to_3d(filler2, z=1, zdir="z")

        home_plate = Rectangle(HOME_PLATE_XY, HOME_PLATE_WIDTH, HOME_PLATE_HEIGHT, color="black", alpha=1, zorder=10, angle=45)
        ax.add_patch(home_plate)
        art3d.pathpatch_2d_to_3d(home_plate, z=1, zdir="z")

        first_base = Rectangle(FIRST_BASE_XY, FIRST_BASE_WIDTH, FIRST_BASE_HEIGHT, color="black", alpha=1, zorder=11, angle=45)
        ax.add_patch(first_base)
        art3d.pathpatch_2d_to_3d(first_base, z=1, zdir="z")

        second_base = Rectangle(SECOND_BASE_XY, SECOND_BASE_WIDTH, SECOND_BASE_HEIGHT, color="black", alpha=1, zorder=12, angle=45)
        ax.add_patch(second_base)
        art3d.pathpatch_2d_to_3d(second_base, z=1, zdir="z")

        third_base = Rectangle(THIRD_BASE_XY, THIRD_BASE_WIDTH, THIRD_BASE_HEIGHT, color="black", alpha=1, zorder=13, angle=45)
        ax.add_patch(third_base)
        art3d.pathpatch_2d_to_3d(third_base, z=1, zdir="z")

        pitchers_plate = Rectangle(PITCHERS_PLATE_XY, PITCHERS_PLATE_WIDTH, PITCHERS_PLATE_HEIGHT, color="black", alpha=1, zorder=14)
        ax.add_patch(pitchers_plate)
        art3d.pathpatch_2d_to_3d(pitchers_plate, z=1, zdir="z")

        x_low=0
        x_high=75
        ax.set_xlim3d(x_low, x_high)
        ax.set_ylim3d((x_high-x_low)/2, -(x_high-x_low)/2)
        ax.set_zlim3d(0, (x_high - x_low) / 2)

        ax.view_init(elev=90, azim=0)
        plt.axis('on')
        ax.set_xlabel('X')

        # adding fielders
        for fielder in lineup.fielders:
            coords = (fielder.coordinates_cartesian.x, fielder.coordinates_cartesian.y)
            radius = 2
            fielder_circle = Circle(coords, radius, color="blue", alpha=1, fill=False)
            ax.add_patch(fielder_circle)
            art3d.pathpatch_2d_to_3d(fielder_circle, z=0, zdir="z")

        # adding balls in play
        for ball in results:
            out = ball[0]
            color = "green" if out else "red"
            flight_path = ball[2]
            path_x = [coord.x for coord in flight_path]
            path_y = [coord.y for coord in flight_path]
            path_z = [coord.z for coord in flight_path]
            ax.plot3D(path_x, path_y, path_z, color)

        # plt.savefig(filename)

        # def sweep():
        #     for i in range(0, 90, 5):
        #         ax.view_init(elev=90, azim=i-45)
        #         plt.savefig(filename + str(i) + ".png")
        # sweep()
        plt.show()

    def __repr__(self):
        pass

