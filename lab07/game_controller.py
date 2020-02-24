from pair_of_dice import PairOfDice

FIRST_ROUND_WIN = [7, 11]
FIRST_ROUND_LOSE = [2, 3, 12]
LOSING_NUM = 7


class GameController:

    def start_play(self):
        pairofdice = PairOfDice()
        # If you roll 7 or 11 on your first roll, you win.
        if pairofdice.current_value() in FIRST_ROUND_WIN:
            print(f"You rolled {pairofdice.current_value()}. You win!")
        # If you roll 2, 3, or 12 on your first role, you lose.
        elif pairofdice.current_value() in FIRST_ROUND_LOSE:
            print(f"You rolled {pairofdice.current_value()}. You lose.")
        # If you roll anything else, that's your 'point', and
        # you keep rolling until you either roll your point
        # again (win) or roll a 7 (lose)
        else:
            point = pairofdice.current_value()
            print(f"Your point is {point}")
            input("Press enter to roll the dice...\n")
            pairofdice.roll_dice()
            while pairofdice.current_value() not in [point, LOSING_NUM]:
                print(f"You rolled {pairofdice.current_value()}.")
                input("Press enter to roll the dice...\n")
                pairofdice.roll_dice()
            if pairofdice.current_value() == point:
                print(f"You rolled {pairofdice.current_value()}. You win!")
            else:
                print(f"You rolled {pairofdice.current_value()}. You lose.")
