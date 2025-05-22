import sys
import random

sys.path.append("D:/Fork/python")
from utils.utils import get_input, play_again


def validate_easy_hard(input_str):
    return input_str.lower() in {"e", "h", "easy", "hard"}


def get_mode():
    return (
        get_input(
            "Choose a difficulty. Type 'easy' or 'hard' (e/h): ",
            validate_easy_hard,
            "Please enter 'e' or 'h'.",
        )
        .lower()
        .startswith("e")
    )


def validate_number(input_str):
    return input_str.isdigit() and int(input_str) > 0 and int(input_str) <= 100


def get_guess(
    message, error_message="Invalid input! Please enter a number between 1 to 100."
):
    return int(get_input(message, validate_number, error_message))


def determine_winner(random_number, guess_number):
    if random_number == guess_number:
        print("Congratulation!")
        return True
    elif random_number < guess_number:
        print("Too high.")
    else:
        print("Too low.")

    return False


def start_game():
    print("Welcome to the Number Guessing Game!\n")

    while True:
        print("I'm thinking of a number between 1 and 100.")

        random_number = random.randint(1, 100)
        attempts_left = 10 if get_mode() else 5

        print(f"You have {attempts_left} attempts remaining to guess the number")

        guess_number = get_guess("Make a guess: ")

        if determine_winner(random_number, guess_number):
            return

        attempts_left -= 1

        while attempts_left > 0:
            guess_number = get_guess("Guess again: ")

            if determine_winner(random_number, guess_number):
                break

            attempts_left -= 1
        else:
            print("You lose!")

        if not play_again():
            print("\nThank you for playing Number Guessing Game!")
            break


if __name__ == "__main__":
    start_game()
