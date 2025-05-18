alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]


def caesar_cipher(text, shift_amount, direction):
    result_text = ""

    for letter in text:
        if letter in alphabet:
            original_position = alphabet.index(letter)
            if direction == "encode":
                new_position = (original_position + shift_amount) % 26
            elif direction == "decode":
                new_position = (original_position - shift_amount) % 26
            result_text += alphabet[new_position]
        else:
            result_text += letter

    print(f"Here is the {direction}d result: {result_text}")


def get_valid_input(prompt, validation_func):
    while True:
        user_input = input(prompt).lower()
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")


def validate_direction(input):
    return input in ["encode", "decode"]


def validate_shift(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


direction = get_valid_input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n", validate_direction
)

text = input("Type your message:\n").lower()

shift = int(get_valid_input("Type the shift number:\n", validate_shift))

caesar_cipher(text, shift, direction)
