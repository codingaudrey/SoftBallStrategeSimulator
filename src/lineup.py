from fielder import Fielder
from src.coordinates import PolarCoordinate


class LineUp:
    def __init__(self, fielders: list[Fielder]):
        self.fielders = fielders

    def add_fielder(self, coordinates: PolarCoordinate) -> None:
        self.fielders.append(Fielder(coordinates))

    def __repr__(self):
        return [fielder.name for fielder in self.fielders]
