from board import Board
from chip import Chip

YELLOW = color(255, 255, 0)
RED = color(249, 16, 0)


class GameController:
    """
    Maintains the state of the game
    and manages interactions of game elements.
    """

    def __init__(self, num_row, num_col, side):
        """Initialize the game controller"""
        self.num_row = num_row
        self.num_col = num_col
        self.side = side
        self.board = Board(self.num_row, self.num_col, self.side)

    def update(self, mouse_pressed, mouse_x, mouse_y):
        """Updates game state on every frame"""

        # Hover the chip
        if mouse_pressed and mouse_y <= self.side:
            col = mouse_x // self.side
            self.board.display_temp_chip(col)

        # Show game board
        self.board.display()

    def handle_mousereleased(self, mouse_x, mouse_y):
        if mouse_y <= self.side:
            col = mouse_x//self.side
            row = self.board.find_avai_row(col)
            if row > 0:
                self.board.add_chip(row, col, mouse_x, mouse_y)
