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
        self.is_over = False

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

    def add_chip(self, row, col):
        if self.is_over:
            return
        chip = Chip(self.side, self.get_player_color(), row * self.side,
                    col * self.side)
        self.chip_count += 1
        self.chips[row][col] = chip
        if self.check_if_win(row, col):
            self.is_over = True
            print("Red wins" if self.is_red else "Yellow wins")
            self.is_red = not self.is_red
            return
        self.is_red = not self.is_red
        print("Computer turn" if not self.is_red else "Red please")
        if self.chip_count >= self.num_row * self.num_col:
            print("The game is over")

    def find_avai_row(self, col):
        for i in range(len(self.chips)):
            if self.chips[i][col]:
                return i - 1
        return i

    def find_avai_cols(self):
        cols = []
        top_row = self.chips[1]
        for i in range(len(top_row)):
            if not top_row[i]:
                cols.append(i)
        return cols

    def check_if_same_color(self, row_1, col_1, row_2, col_2):
        try:
            chip_1 = self.chips[row_1][col_1]
            chip_2 = self.chips[row_2][col_2]
            if not chip_2 or chip_1.chip_color != chip_2.chip_color:
                return False
            return True
        except IndexError:
            return False

    def check_if_win(self, row, col):
        # check 4 in a row horizontally
        for i in range(- 3, 1):
            if (self.check_if_same_color(row, col, row, col + i) and
                self.check_if_same_color(row, col, row, col + i + 1) and
                self.check_if_same_color(row, col, row, col + i + 2) and
                self.check_if_same_color(row, col, row, col + i + 3)):
                return True

        # check 4 in a row vertically
        if (self.check_if_same_color(row, col, row + 1, col) and
           self.check_if_same_color(row, col, row + 2, col) and
           self.check_if_same_color(row, col, row + 3, col)):
            return True

        # check 4 in a row diagonally from top left to bottom right
        for i in range(- 3, 1):
            if (self.check_if_same_color(row, col, row + i, col + i) and
                self.check_if_same_color(row, col, row + i + 1, col + i + 1)
                and
                self.check_if_same_color(row, col, row + i + 2, col + i + 2)
                and
                self.check_if_same_color(row, col, row + i + 3, col + i + 3)):
                return True

        # check 4 in a row diagonally from bottom left to top right
        for i in range(- 3, 1):
            if (self.check_if_same_color(row, col, row - i, col + i) and
                self.check_if_same_color(row, col, row - i - 1, col + i + 1)
                and
                self.check_if_same_color(row, col, row - i - 2, col + i + 2)
                and
                self.check_if_same_color(row, col, row - i - 3, col + i + 3)):
                return True
