import time
import functools


def get_valid_input(
    prompt, validation_func, error_message="Invalid input. Please try again."
):
    while True:
        user_input = input(prompt).strip().lower()
        if validation_func(user_input):
            return user_input
        print(error_message)


def get_input(
    prompt, error_message="Invalid input. Please try again.", case_sensitive=False
):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_message)
            continue

        return user_input if case_sensitive else user_input.lower()


def validate_number_v1(input_str):
    return input_str.isdigit()


def validate_number_v2(input_str):
    return input_str.isdigit() and int(input_str) > 0


def validate_yes_no(input_str):
    return input_str.lower() in {"y", "n", "yes", "no"}


def process_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    return wrapper


def play_again():
    return (
        get_input("\nPlay again? (y/n): ", validate_yes_no, "Please enter 'y' or 'n'.")
        .lower()
        .startswith("y")
    )
