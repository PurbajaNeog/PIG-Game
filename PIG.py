# PIG-Game
import random as rd

from dice import dice


current_sum = 0


def roll(user_score, computer_score, dice_number):
    global current_sum

    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    print(dice[dice_number])
    if dice_number != 1:
        current_sum += dice_number
        print(f"Turn Total: {current_sum}\n")
    else:
        current_sum = 0
        print(f"Turn Total: {current_sum}\n")


def main():
    global current_sum
    turns = 0
    start = rd.choice(["user", "computer"])
    while True:
        user_score = 0
        computer_score = 0

        initial = input("Welcome to the PIG-Game:\n1. Play\n2. Exit\nYour Choice: ")

        if initial == "1":
            while True:
                diceNum = rd.randint(1, 6)
                computer_choice = rd.choice(["r", "h"])
                print(f"\nTurns: {turns}({start})")
                if start == "user":
                    user_input = input(f"Your Turn:\nRoll(r)\tHold(h)\n").lower()
                    if user_input == "r":
                        roll(user_score, computer_score, diceNum)
                        print(f"Your Score: {user_score}")
                        print(f"Computer Score: {computer_score}")

                    elif user_input == "h":
                        print(f"{current_sum} was added to your score({user_score}). Current score is ")
                        user_score += current_sum
                        current_sum = 0
                        print(f"Your Score: {user_score}")
                        print(f"Computer Score: {computer_score}")

                    else:
                        print("Invalid Input")

                    if diceNum == 1 or user_input == "h":
                        start = "computer"
                        turns += 1

                else:
                    print(f"Computer's Turn")
                    if current_sum >= 0 or computer_choice == "r":
                        roll(user_score, computer_score, diceNum)
                        print(f"Your Score: {user_score}")
                        print(f"Computer Score: {computer_score}")

                    if computer_choice == "h":
                        print(f"{current_sum} was added to computer's score({computer_score}). Current score is ")
                        computer_score += current_sum
                        current_sum = 0
                        print(f"Your Score: {user_score}")
                        print(f"Computer Score: {computer_score}")

                    if diceNum == 1 or computer_choice == "h":
                        start = "user"
                        turns += 1
                
                if user_score >= 100:
                    print("Congratulations! You Won🕺😊")
                    break

                elif computer_score >= 100: 
                    print("Computer Won🤖. Better luck next time😊.")
                    break

        elif initial == "2":
            break

        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
