from game_controller import GameController


def print_game_des():
    print("--------------------------------")
    print("Welcome to street craps!\n")
    print("Rules:")
    print("If you roll 7 or 11 on your first roll, you win.")
    print("If you roll 2, 3, or 12 on your first role, you lose.")
    print("If you roll anything else, that's your 'point', and")
    print("you keep rolling until you either roll your point")
    print("again (win) or roll a 7 (lose)\n")


def main():
    gc = GameController()  # create an instance of class GameController
    print_game_des()
    input("Press enter to roll the dice...\n")
    gc.start_play()  # use method start_play to play game


main()
