from lineup import LineUp
from fielder import Fielder
from ball_in_play import BallInPlay
from constants import DEFAULT_INTERVAL_MS
from constants import DEFAULT_FIELDER_HEIGHT
from src.coordinates import CartesianCoordinate


class CatchCalculator:
    def __init__(self):
        pass

    @staticmethod
    def calculate_out_fielder(fielder: Fielder, ball_in_play: BallInPlay, flight_path: list[CartesianCoordinate]) \
            -> [bool, list[CartesianCoordinate]]:
        radii = fielder.get_radii()
        out = False
        intersections = []
        for t in range(len(ball_in_play.path)):
            ball = ball_in_play.path[t]
            if 0 < ball.z < DEFAULT_FIELDER_HEIGHT \
                    and fielder.coordinates_cartesian.x - radii[t][0] < ball.x < fielder.coordinates_cartesian.x + radii[t][0] \
                    and fielder.coordinates_cartesian.y - radii[t][0] < ball.y < fielder.coordinates_cartesian.y + radii[t][0]:
                out = True
                intersections.append(ball)
        ball_in_play.caught = out
        return out, intersections

    @staticmethod
    def calculate_out_lineup(lineup: LineUp, flight_path: list[CartesianCoordinate]) -> [bool, list[(str, CartesianCoordinate)]]:
        out = False
        intersections = []
        for fielder in lineup.fielders:
            caught, positions = CatchCalculator.calculate_out_fielder(fielder, flight_path)
            if caught:
                out = True
                intersections.append((fielder.name, positions))
        return out, intersections, flight_path

    @staticmethod
    def calculate_multiple(lineup: LineUp, balls_in_play: list[BallInPlay]) \
            -> list[[bool, list[(str, CartesianCoordinate)], list[CartesianCoordinate]]]:
        return_value = []
        for ball in balls_in_play:
            return_value.append(CatchCalculator.calculate_out_lineup(lineup, ball.path))
        return return_value


if __name__ == '__main__':
    ball_in_play = BallInPlay(10, 0, 0, 2)
    balls = []
    for height in range(3):
        balls.append(BallInPlay(10, 0, 0, height))
    # print(ball_in_play.path_3d())
    # fielder = Fielder(CartesianCoordinate(2, 0, 0))
    # print(fielder)
    # print(CatchCalculator.calculate_out_fielder(fielder, ball_in_play))
    fielders = []
    for distance in range(3):
        fielders.append(Fielder(CartesianCoordinate(distance, 0, 0), False))
    lineup = LineUp(fielders)
    # print(CatchCalculator.calculate_out_lineup(lineup, ball_in_play.path_3d()))
    calc_multiple_result = CatchCalculator.calculate_multiple(lineup, balls)
    caught = False
    for result in calc_multiple_result:
        if result[0]:
            caught = True
            break
    print(caught)
    print(calc_multiple_result)


