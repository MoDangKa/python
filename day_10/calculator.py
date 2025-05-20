import sys

sys.path.append("D:/Fork/python")
from utils.utils import get_valid_input, validate_number


def validate_operation(input_str):
    return input_str in ["+", "-", "*", "/"]


def get_operation():
    return get_valid_input(
        "\nAvailable operations:\n+   -   *   /\nPick an operation: ",
        validate_operation,
        "Invalid operation. Please enter '+', '-', '*' or '/'.",
    )


def validate_yes_no(input_str):
    return input_str.lower() in {"y", "n", "yes", "no"}


def should_continue(current_value):
    response = get_valid_input(
        f"\nCurrent result: {current_value}\n" "Continue with this result? (y/n): ",
        validate_yes_no,
        "Please enter 'y' or 'n'.",
    ).lower()
    return response.startswith("y")


def perform_calculation(a, b, operator):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else float("nan"),
    }
    return operations[operator](a, b)


def calculator():
    print("Welcome to the Python Calculator!")

    while True:
        a = int(
            get_valid_input(
                "\nWhat's the first number?: ",
                validate_number,
                "Please enter a valid whole number.",
            )
        )

        while True:
            operator = get_operation()
            b = int(
                get_valid_input(
                    "What's the next number?: ",
                    validate_number,
                    "Please enter a valid whole number.",
                )
            )

            result = perform_calculation(a, b, operator)

            if operator == "/" and b == 0:
                print("Error: Division by zero!")
                continue

            print(f"\n{a} {operator} {b} = {result}")
            a = result

            if not should_continue(a):
                break

        new_calc = get_valid_input(
            "\nStart a new calculation? (y/n): ",
            validate_yes_no,
            "Please enter 'y' or 'n'.",
        ).lower()

        if not new_calc.startswith("y"):
            print("\nThank you for using the calculator!")
            break


if __name__ == "__main__":
    calculator()
