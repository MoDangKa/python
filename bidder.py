def get_valid_input(
    prompt, validation_func, error_message="Invalid input. Please try again."
):
    while True:
        user_input = input(prompt).strip().lower()
        if validation_func(user_input):
            return user_input
        print(error_message)


def validate_bid(input_str):
    return input_str.isdigit() and int(input_str) > 0


def validate_yes_no(input_str):
    return input_str in ["yes", "no", "y", "n"]


def get_name():
    while True:
        name = input("What is your name?: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_bid():
    bid_str = get_valid_input(
        "What is your bid?: $",
        validate_bid,
        "Please enter a positive whole number for your bid.",
    )
    return int(bid_str)


def should_continue_bidding():
    response = get_valid_input(
        "Are there any other bidders? Type 'yes' or 'no': ",
        validate_yes_no,
        "Please enter 'yes' or 'no'.",
    )
    return response in ["yes", "y"]


def open_bidding():
    bids = {}

    while True:
        name = get_name()
        bid = get_bid()
        bids[name] = bid

        if not should_continue_bidding():
            break

    return bids


def main():
    print("Welcome to the Silent Auction!")
    bids = open_bidding()

    if bids:
        winner = max(bids, key=bids.get)
        print(f"\nAuction ended! The winner is {winner} with a bid of ${bids[winner]}.")
    else:
        print("No bids were placed.")


if __name__ == "__main__":
    main()
