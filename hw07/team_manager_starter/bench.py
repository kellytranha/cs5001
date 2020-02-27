FIFO = 0


class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        # Initialize the bench object with whatever
        # attributes and values it will need
        self.bench = []

    def send_to_bench(self, player):
        # Put the player "onto the bench"
        self.bench.append(player)

    def get_from_bench(self):
        # Return the name of the player who has
        # been on the bench longest.
        return self.bench.pop(FIFO)

    def show_bench(self):
        # Write the function that will display the
        # current list of players on the bench
        if self.bench:
            print("The bench currently includes:")
            for player in self.bench:
                print(player)
        else:
            print("The bench is empty.")

    def cut_from_bench(self, player):
        if player in self.bench:
            self.bench.remove(player)
