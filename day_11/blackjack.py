import sys
import random

sys.path.append("D:/Fork/python")
from blackjack_arts import BLACKJACK_LOGO, get_card_art
from utils.utils import get_input, validate_yes_no


def create_deck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    value = 0
    aces = 0

    for card in hand:
        card_value = card[0]
        if card_value == 1:
            aces += 1
            value += 11
        elif card_value >= 10:
            value += 10
        else:
            value += card_value

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value


def display_hand(hand, title):
    print(f"\n{title}:")
    cards_art = [get_card_art(card[0], card[1]).split("\n") for card in hand]
    for i in range(7):
        print(" ".join(card[i] for card in cards_art))


def get_another_card():
    return (
        get_input(
            "\nDo you want another card? (y/n): ",
            validate_yes_no,
            "Please enter 'y' or 'n'.",
        )
        .lower()
        .startswith("y")
    )


def dealer_plays(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand


def check_blackjack(hand):
    return len(hand) == 2 and calculate_hand_value(hand) == 21


def display_card_and_total(hand=[], title="On hand", message="Total:"):
    display_hand(hand, title)
    print(message, calculate_hand_value(hand))


def determine_winner(player_hand, dealer_hand):
    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    player_bj = check_blackjack(player_hand)
    dealer_bj = check_blackjack(dealer_hand)

    if player_bj and dealer_bj:
        return "Both have Blackjack! Push"
    elif player_bj:
        return "Blackjack! You win!"
    elif dealer_bj:
        return "Dealer has Blackjack! You lose!"

    if player_total > 21:
        return "You busted! You lose!"
    elif dealer_total > 21:
        return "Dealer busted! You win!"
    elif player_total > dealer_total:
        return "You win!"
    elif player_total < dealer_total:
        return "You lose!"
    else:
        return "Push"


def play_again():
    """Ask if player wants to play another game"""
    return (
        get_input("\nPlay again? (y/n): ", validate_yes_no, "Please enter 'y' or 'n'.")
        .lower()
        .startswith("y")
    )


def play_blackjack():
    print(BLACKJACK_LOGO)
    while True:
        deck = create_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        if check_blackjack(player_hand):
            display_card_and_total(dealer_hand, "Dealer's hand", "Dealer total:")
            display_card_and_total(player_hand, "Your hand", "Your total:")
            print("\nBlackjack! You win!")
            if not play_again():
                return
            continue

        display_card_and_total([dealer_hand[0]], "Dealer's hand", "Dealer's showing:")
        while True:
            display_card_and_total(player_hand, "Your hand", "Your total:")

            if calculate_hand_value(player_hand) > 21:
                print("\nYou've busted!")
                break

            if not get_another_card():
                break

            player_hand.append(deck.pop())

        if calculate_hand_value(player_hand) <= 21:
            dealer_hand = dealer_plays(deck, dealer_hand)

        print("\n------------------------------------")
        display_card_and_total(dealer_hand, "Dealer's hand", "Dealer total:")
        display_card_and_total(player_hand, "Your hand", "Your total:")
        print("------------------------------------\n")

        result = determine_winner(player_hand, dealer_hand)
        print(result)

        if not play_again():
            print("\nThank you for playing Blackjack!")
            break


if __name__ == "__main__":
    play_blackjack()
