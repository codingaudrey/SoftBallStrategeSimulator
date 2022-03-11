import math
from constants import DEFAULT_INTERVAL_MS

DEFAULT_JERK = 3
DEFAULT_V_MAX = 5.3
DEFAULT_GLOVE_SPEED = 2.0

DEFAULT_DURATION_MS = 10000  # miliseconds
# DEFAULT_INTERVAL = .1


class RadiusManager:
    def __init__(self, jerk=DEFAULT_JERK, v_max=DEFAULT_V_MAX, glove_speed=DEFAULT_GLOVE_SPEED):
        self.jerk = jerk
        self.v_max = v_max
        self.glove_speed = glove_speed

    def get_radius(self, t: float) -> float:
        return t * self.v_max * math.tanh(t/self.jerk) + min(self.glove_speed*t, self.glove_speed/2)

    def get_radii(self, total_time=DEFAULT_DURATION_MS, dt=DEFAULT_INTERVAL_MS) -> list[tuple[float, float]]:
        t = 0
        radii = [(0, t)]
        while t < total_time:
            t += dt
            radii.append((self.get_radius(t/1000), t))
        return radii

    def __repr__(self):
        return_string = f"jerk :{self.jerk}\n"
        return_string += f"velocity max: {self.v_max}\n"
        return_string += f"glove speed: {self.glove_speed}\n"
        return return_string


# print(RadiusManager().get_radii())
