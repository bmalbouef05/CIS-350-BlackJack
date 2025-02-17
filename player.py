from hand import Hand

class Player:
    def __init__(self, is_person):
        self.is_person = is_person
        self.hand = Hand()

    def hit(self, card):
        self.hand.draw_card(card)

    def stand(self):
        pass

    def get_hand(self):
        return self.hand
