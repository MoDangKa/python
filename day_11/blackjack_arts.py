BLACKJACK_LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# BLACKJACK_LOGO = """
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
#       |  \\/ K|                            _/ |                
#       `------'                           |__/           
# """


def get_card_art(value, suit):
    if value == 11:
        display_value = "J"
    elif value == 12:
        display_value = "Q"
    elif value == 13:
        display_value = "K"
    elif value == 1:
        display_value = "A"
    else:
        display_value = str(value)

    suit_symbols = {"hearts": "♥", "diamonds": "♦", "clubs": "♣", "spades": "♠"}
    symbol = suit_symbols.get(suit, "?")

    card = f"""
    ┌─────────┐
    │ {display_value:<2}      │
    │         │
    │    {symbol}    │
    │         │
    │      {display_value:>2} │
    └─────────┘
    """
    return card
