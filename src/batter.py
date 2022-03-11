from hit_distribution import HitDistribution
from ball_in_play import BallInPlay


class Batter:
    def __init__(self, hit_distribution: HitDistribution, name=""):
        self.hit_distribution = hit_distribution

    def swing(self, count=1) -> list[BallInPlay]:
        return self.hit_distribution.generate_balls_in_play(count)

    def __repr__(self):
        return self.hit_distribution
