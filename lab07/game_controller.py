from pair_of_dice import PairOfDice

FIRST_ROUND_WIN = [7, 11]
FIRST_ROUND_LOSE = [2, 3, 12]
LOSING_NUM = 7


class GameController:

    def start_play(self):
        pairofdice = PairOfDice()

        if pairofdice.current_value() in FIRST_ROUND_WIN:
            print(f"You rolled {pairofdice.current_value()}. You win!")
        elif pairofdice.current_value() in FIRST_ROUND_LOSE:
            print(f"You rolled {pairofdice.current_value()}. You lose.")
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
