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


def validate_number(input_str):
    return input_str.isdigit() and int(input_str) > 0
