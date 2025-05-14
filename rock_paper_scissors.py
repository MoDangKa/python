import random

# ASCII art for rock, paper, and scissors
ascii_art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """,
}


# Function for the game
def play_game():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")

    # Get user's choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        return

    # Get computer's choice
    computer_choice = random.choice(options)

    # Show choices with ASCII art
    print("\nYou chose:")
    print(ascii_art[user_choice])
    print("Computer chose:")
    print(ascii_art[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")


# Run the game
play_game()
