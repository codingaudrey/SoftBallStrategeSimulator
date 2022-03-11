from random import Random


class ID:
    def __init__(self, _id=None):
        self.id = str(_id) if _id else self.new_id()

    @staticmethod
    def new_id():
        rand = Random()
        return str(rand.randint(0, 2**64))

    def get_id(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return self.id