from chip import Chip

GREY = color(204, 204, 204)
BLUE = color(0, 0, 204)
YELLOW = color(255, 255, 0)
RED = color(249, 16, 0)
WEIGHT_FACTOR = 10


class Board:
    """A game board"""
    def __init__(self, num_row, num_col, side):
        """Initialize the game controller"""
        self.num_row = num_row
        self.num_col = num_col
        self.side = side
        self.stroke_weight = side/WEIGHT_FACTOR
        self.chips = [[None] * num_col for _ in range(num_row + 1)]
        self.is_red = True
        self.chip_count = 0

    def display(self):
        for row in self.chips:
            for cell in row:
                if cell:
                    cell.display()
        strokeWeight(self.stroke_weight)
        stroke(BLUE)
        noFill()
        for j in range(1, self.num_row + 1):
            for i in range(self.num_col):
                square(i * self.side, j * self.side, self.side)

    def get_player_color(self):
        if self.is_red:
            return RED
        else:
            return YELLOW

    def display_temp_chip(self, col):
        fill(self.get_player_color())
        strokeWeight(0)
        ellipse(col * self.side, 0, self.side, self.side)

    def add_chip(self, row, col, mouse_x, mouse_y):
        chip = Chip(self.side, self.get_player_color(), row * self.side,
                    col * self.side, mouse_y)
        self.chip_count += 1
        self.chips[row][col] = chip
        self.is_red = not self.is_red
        if self.chip_count >= self.num_row * self.num_col:
            print("The game is over")

    def find_avai_row(self, col):
        for i in range(len(self.chips)):
            if self.chips[i][col]:
                return i - 1
        return i
