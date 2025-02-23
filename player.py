from hand import Hand
from card import Card

class Player:
    def __init__(self, is_person):

        # Boolean variable to check whether it's a person or the dealer

        self.is_person = is_person

        # Init the player's hand object

        self.hand = Hand()

        # Variable to check whether or not the player is standing (not taking any more turns)

        self.is_standing = False

        # Check to see if player just drew cards

        self.drew_card = True

    def hit(self, card):
        

        if type(card) != Card:
            return
        else:
            # Just adds the "hit" card to the current hand

            self.hand.draw_card(card)
            self.drew_card = True

    def stand(self):
        self.is_standing = True

    def get_hand(self):
        return self.hand
