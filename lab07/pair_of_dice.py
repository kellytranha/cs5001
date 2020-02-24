from die import Die


class PairOfDice:  # create a class PairOfDice
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        # roll each die
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        # return current value
        return self.die1.current_value + self.die2.current_value
