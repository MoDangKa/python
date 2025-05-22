import sys
import random

MAX_NUMBER = 100
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

sys.path.append("D:/Fork/python")
from utils.utils import get_input, play_again


def validate_easy_hard(input_str: str) -> bool:
    """Validate difficulty level input."""
    return input_str.lower() in {"e", "h", "easy", "hard"}


def get_mode() -> bool:
    """Get game difficulty mode from user."""
    return (
        get_input(
            "Choose a difficulty. Type 'easy' or 'hard' (e/h): ",
            validate_easy_hard,
            "Please enter 'e' or 'h'.",
        )
        .lower()
        .startswith("e")
    )


def validate_number(input_str: str) -> bool:
    """Validate the guessed number is within range."""
    if not input_str.isdigit():
        return False
    number = int(input_str)
    return 1 <= number <= MAX_NUMBER


def get_guess(remaining_attempts: int) -> int:
    """Get and validate user's guess."""
    message = f"Make a guess (1-{MAX_NUMBER}), {remaining_attempts} attempts left: "
    error_msg = f"Invalid input! Please enter a number between 1 and {MAX_NUMBER}."
    return int(get_input(message, validate_number, error_msg))


def give_feedback(secret: int, guess: int) -> bool:
    """Provide feedback on the guess and return if it was correct."""
    if secret == guess:
        print("Congratulations! You guessed it right!")
        return True
    elif secret > guess:
        print("Too low.")
    else:
        print("Too high.")
    return False


def start_game_round() -> bool:
    """Run a single round of the guessing game."""
    secret_number = random.randint(1, MAX_NUMBER)
    attempts = EASY_ATTEMPTS if get_mode() else HARD_ATTEMPTS

    print(f"I'm thinking of a number between 1 and {MAX_NUMBER}.")
    print(f"You have {attempts} attempts to guess the number.\n")

    while attempts > 0:
        guess = get_guess(attempts)

        if give_feedback(secret_number, guess):
            return True

        attempts -= 1
        if attempts > 0:
            print(f"Attempts remaining: {attempts}")

    print(f"\nSorry, you've run out of attempts. The number was {secret_number}.")
    return False


def start_game():
    """Main game loop with replay functionality."""
    print("Welcome to the Number Guessing Game!\n")

    while True:
        start_game_round()

        if not play_again():
            print("\nThank you for playing the Number Guessing Game!")
            break


if __name__ == "__main__":
    start_game()
