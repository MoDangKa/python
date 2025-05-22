import sys
import random

sys.path.append("D:/Fork/python")
from utils.utils import get_input, play_again


def validate_easy_hard(input_str):
    return input_str.lower() in {"e", "h", "easy", "hard"}


def get_mode():
    choice = get_input(
        "Choose a difficulty. Type 'easy' or 'hard' (e/h): ",
        validate_easy_hard,
        "Please enter 'e' or 'h'.",
    ).lower()
    return choice.startswith("e")


def validate_number(input_str):
    return input_str.isdigit() and 1 <= int(input_str) <= 100


def get_guess(message):
    return int(
        get_input(
            message,
            validate_number,
            "Invalid input! Please enter a number between 1 and 100.",
        )
    )


def start_game():
    print("Welcome to the Number Guessing Game!\n")

    while True:
        print("I'm thinking of a number between 1 and 100.")
        random_number = random.randint(1, 100)
        attempts_left = 10 if get_mode() else 5
        guessed_numbers = set()

        while attempts_left > 0:
            print(f"\nYou have {attempts_left} attempt(s) remaining.")
            guess = get_guess("Make a guess: ")

            if guess in guessed_numbers:
                print("You've already guessed that number. Try a different one!")
                continue

            guessed_numbers.add(guess)

            if guess == random_number:
                print(f"Congratulations! You guessed the number {random_number}. 🎉")
                break
            elif guess < random_number:
                print("Too low.")
            else:
                print("Too high.")

            attempts_left -= 1
        else:
            print(
                f"\nYou've run out of attempts! The correct number was {random_number}. 😢"
            )

        if not play_again():
            print("\nThank you for playing the Number Guessing Game!")
            break


if __name__ == "__main__":
    start_game()
