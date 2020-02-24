import random

DIE_MIN = 1
DIE_MAX = 6


class Die:  # create class Die to create a dice
    def __init__(self):
        self.roll()

    def roll(self):
        self.current_value = random.randint(DIE_MIN, DIE_MAX)

    def __repr__(self):
        return str(self.current_value)
