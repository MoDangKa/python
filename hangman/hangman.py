import random
import re

# import hangman_words
from hangman_words import word_list
from hangman_arts import stages, logo_b


# chosen_word = random.choice(hangman_words.word_list)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
placeholder = ["_" for _ in chosen_word]
score = 0
life_point = 6
guess = ""
guess_letters = []
wrong_letters = []


def show_placeholder():
    print(" ".join(placeholder))


def get_guess():
    global guess
    while True:  # Loop until valid input is entered
        guess = input("Guess a letter: ").lower()

        if re.search(r"^[a-z]$", guess):  # Ensure input is a single letter
            return True
        else:
            print("Invalid input! Please enter only **one** letter.")


def check_letter():
    global score, life_point, wrong_letters

    if guess in guess_letters:
        print("-------------------------------------")
        print("You've already guessed this letter.")
        return

    guess_letters.append(guess)
    guess_letters.sort()

    correct_guess = False

    for number in range(word_length):
        if chosen_word[number] == guess:
            if placeholder[number] == "_":
                placeholder[number] = guess
                score += 1

            correct_guess = True

    if not correct_guess:
        life_point -= 1
        wrong_letters.append(guess)
        wrong_letters.sort()


def handle_wrong_letter():
    wrong_list = " ".join(wrong_letters) if wrong_letters else "empty"
    print(f"Wrong letters: {wrong_list}")


def start_hangman_game():
    print(logo_b)

    while score < word_length and life_point > 0:
        print(stages[life_point])
        show_placeholder()

        is_pass = get_guess()
        if not is_pass:
            continue  # Retry input instead of exiting game

        check_letter()

        print("-------------------------------------")
        print(f"Guess letters: {" ".join(guess_letters)}")
        handle_wrong_letter()
        print("-------------------------------------")

    if score == word_length:
        print("🎉 You win!")
    elif life_point <= 0:
        print(stages[life_point])
        print(f"💀 You lose! The word was: **{chosen_word}**")


start_hangman_game()
