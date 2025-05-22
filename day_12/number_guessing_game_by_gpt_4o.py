import sys
import random

sys.path.append("D:/Fork/python")
from utils.utils import get_input, play_again

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


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
    return input_str.isdigit() and 1 <= int(input_str) <= 100


def get_guess(
    message, error_message="Invalid input! Please enter a number between 1 to 100."
):
    return int(get_input(message, validate_number, error_message))


def determine_winner(target, guess):
    if target == guess:
        print("Congratulations! You guessed the number correctly!")
        return True
    elif target > guess:
        print("Too low.")
    else:
        print("Too high.")
    return False


def start_game():
    print("Welcome to the Number Guessing Game!\n")

    while True:
        print("I'm thinking of a number between 1 and 100.")
        target_number = random.randint(1, 100)

        # Choose difficulty
        is_easy_mode = get_mode()
        max_attempts = EASY_ATTEMPTS if is_easy_mode else HARD_ATTEMPTS
        attempts_left = max_attempts

        print(f"You have {attempts_left} attempts to guess the number.")

        while attempts_left > 0:
            guess = get_guess("Make a guess: ")
            if determine_winner(target_number, guess):
                break
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Attempts remaining: {attempts_left}")
            else:
                print(
                    f"Sorry, you've run out of attempts. The number was {target_number}."
                )

        if not play_again():
            print("\nThank you for playing Number Guessing Game!")
            break


if __name__ == "__main__":
    start_game()
