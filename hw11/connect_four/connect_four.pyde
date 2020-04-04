from game_controller import GameController

NUM_ROW = 2
NUM_COL = 2
SIDE = 90
SPACE = {'w': NUM_COL * SIDE, 'h': NUM_ROW * SIDE + SIDE}
GREY = color(204, 204, 204)

game_controller = GameController(NUM_ROW, NUM_COL, SIDE)

def setup():
    size(SPACE['w'], SPACE['h']) 
    ellipseMode(CORNER)

def draw():
    background(GREY)
    game_controller.update(mousePressed, mouseX, mouseY)

def mouseReleased():
    game_controller.handle_mousereleased(mouseX, mouseY)

    
