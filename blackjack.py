import random

# Card deck with values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

class BlackjackGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")
        
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        
        self.init_ui()
        self.new_game()
    
    def create_deck(self):
        pass
    
    def deal_card(self, hand):
        pass
    
    def calc_hand(self, hand):
        pass
    
    
    def hit(self):
       pass
    
    def stand(self):
       pass
    
    
    def new_game(self):
        pass
    

if __name__ == "__main__":