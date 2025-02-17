from hand import Hand

class Player:
    def __init__(self, is_person):
        self.is_person = is_person
        self.hand = Hand()