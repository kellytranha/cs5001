

class Player:
    """A class representing a dodgeball player"""
    def __init__(self, name, number, position):
        self.name = name
        self.number = number
        self.position = position

    def __repr__(self):
        return self.name

    # Write a constructor (__init__() method) that
    # will take the necessary values, set them to
    # the player object's attributes, and create the
    # new instance of player. Like all methods, its first
    # parameter must be `self`. The remaining parameters should
    # receive whatever pieces of data are relevant to creating
    # a new Player object.
