from batter import Batter
from lineup import LineUp
from constants import DEFAULT_BALLS_IN_PLAY
from catch_calculator import CatchCalculator
from hit_distribution import HitDistribution
from math import pi
from fielder import Fielder
from coordinates import PolarCoordinate
from animator import Animator


class Main:
    def __init__(self, batter: Batter, lineup: LineUp, count=DEFAULT_BALLS_IN_PLAY):
        self.batter = batter
        self.lineup = lineup
        self.balls_in_play = self.batter.hit_distribution.generate_balls_in_play(count)
        self.results = CatchCalculator.calculate_multiple(self.lineup, self.balls_in_play)

    def animate_results(self, filename) -> None:
        Animator.single_image(filename, self.lineup, self.results)

    def __repr__(self):
        return_string = f"batter: {self.batter}\n"
        return_string += f"lineup: {self.lineup}\n"
        return_string += f"balls in play: {self.balls_in_play}\n"
        return_string += f"results: {self.results}\n"
        return return_string


if __name__ == '__main__':
    batter = Batter(HitDistribution(25, 3, -pi/8, pi/12, pi/8, pi/16))
    pitcher = Fielder(PolarCoordinate(15.24, 0))
    base_1 = Fielder(PolarCoordinate(22, pi/5))
    base_2 = Fielder(PolarCoordinate(30, pi/10))
    short = Fielder(PolarCoordinate(30, -pi/10))
    base_3 = Fielder(PolarCoordinate(22, -pi/5))
    mf = Fielder(PolarCoordinate(46, -pi/10))
    lf = Fielder(PolarCoordinate(60, -pi*3/16))
    lc = Fielder(PolarCoordinate(67, -pi/16))
    rc = Fielder(PolarCoordinate(60, pi/16))
    rf = Fielder(PolarCoordinate(60, pi*3/16))
    lineup = LineUp([pitcher, base_1, base_2, short, base_3, lf, lc, rc, mf])
    main = Main(batter, lineup)
    results = main.results
    print(results)
    main.animate_results("animation_test.png")
