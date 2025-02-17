from card import Card
import random

class Deck:
    def __init__(self):
        self.current_deck = []

        available_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        available_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        for i in available_ranks:
            for j in available_suits:
                self.current_deck.append(Card(j, i))

    def reset_deck(self):
        self.current_deck = []

        available_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        available_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        for i in available_ranks:
            for j in available_suits:
                self.current_deck.append(Card(j, i))

    def deal_card(self):
        index_to_take = random.randint(0, (len(self.current_deck) - 1))
        card_to_deal = self.current_deck.pop(index_to_take)
        return card_to_deal


