from card import Card
import random

class Deck:
    def __init__(self):
        self.current_deck = []

        available_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        available_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        # Loop through all available ranks and suits and add a card of every combination
        # To the current deck (initializes the deck)

        for i in available_ranks:
            for j in available_suits:
                self.current_deck.append(Card(j, i))

    def reset_deck(self):
        
        # Same set up as the original initialization
        
        self.current_deck = []

        available_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        available_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        # Loop through all available ranks and suits and add a card of every combination
        # To the current deck (initializes the deck)

        for i in available_ranks:
            for j in available_suits:
                self.current_deck.append(Card(j, i))

    def deal_card(self):

        # Instead of "shuffling" the deck, I have it randomly choose a card from the sorted deck
        # and return that card as a way of dealing it.

        index_to_take = random.randint(0, (len(self.current_deck) - 1))
        card_to_deal = self.current_deck.pop(index_to_take)
        return card_to_deal


