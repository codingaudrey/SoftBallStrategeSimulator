from ball_in_play import BallInPlay
from numpy import random


class HitDistribution:
    def __init__(self, velocity_average: float, velocity_variance: float,
                 horizontal_angle_average: float, horizontal_angle_variance: float,
                 vertical_angle_average: float, vertical_angle_variance: float):
        self.velocity_avg = velocity_average
        self.velocity_var = velocity_variance
        self.horiz_avg = horizontal_angle_average
        self.horiz_var = horizontal_angle_variance
        self.vert_avg = vertical_angle_average
        self.vert_var = vertical_angle_variance
        self.starting_height = 1

    def generate_balls_in_play(self, count: int) -> list[BallInPlay]:
        balls_in_play = []
        for _ in range(count):
            velocity = random.normal(self.velocity_avg, self.velocity_var)
            horizontal_angle = random.normal(self.horiz_avg, self.horiz_var)
            vertical_angle = random.normal(self.vert_avg, self.vert_var)
            balls_in_play.append(BallInPlay(velocity, vertical_angle, horizontal_angle, self.starting_height))
        return balls_in_play

    def __repr__(self):
        return_string = ""
        return_string += f"Velocity average: {self.velocity_avg}\nVelocity variance: {self.velocity_var}\n"
        return_string += f"Horizontal angle average: {self.horiz_avg}\nHorizontal angle variance: {self.horiz_var}\n"
        return_string += f"Vertical angle average: {self.vert_avg}\nVertical Angle variance: {self.vert_var}\n"
