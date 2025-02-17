
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.blackjack_val = CARD_VALUES[rank]
        self.suit = suit

    def get_blackjack_value(self):
        return self.blackjack_val
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"