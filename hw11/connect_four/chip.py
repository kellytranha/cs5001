ADDED_PIXEL = 40


class Chip:
    """A playing disk"""
    def __init__(self, radius, chip_color, y, x, mouse_y):
        """Initialize the game controller"""
        self.radius = radius
        self.chip_color = chip_color
        self.x = x
        self.y = y
        self.mouse_y = mouse_y

    def display(self):
        fill(self.chip_color)
        strokeWeight(0)
        if self.mouse_y >= self.y - ADDED_PIXEL:
            self.mouse_y = self.y
        else:
            self.mouse_y += ADDED_PIXEL
        ellipse(self.x, self.mouse_y, self.radius, self.radius)
