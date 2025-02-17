import random
import pygame as py
from display import Display
from deck import Deck
from player import Player


class BlackjackGame:
    def __init__(self):

        # Initialize the Deck and both the Player and Dealer classes

        self.deck = Deck()
        self.player = Player(True)
        self.dealer = Player(False)
        
        # 0 = Player, 1 = Dealer
        self.current_turn = 0
        
        # self.init_ui()
        self.new_game()
    
    def deal_start_cards(self):
        
        # Make a new deck and make sure the player goes first

        self.deck.reset_deck()
        self.current_turn = 0

        # Draws two cards per player to start off

        self.player.hand.draw_card(self.deck.deal_card())
        self.player.hand.draw_card(self.deck.deal_card())
        self.dealer.hand.draw_card(self.deck.deal_card())
        self.dealer.hand.draw_card(self.deck.deal_card())

    def player_turn(self):
        self.current_turn = 1

        # Needs to be implemented

        pass


    def dealer_turn(self):

        # Will check if the player/dealer is standing in the game loop
        
        # If the dealer has either blackjack or bust, they "stand" (don't take any more turns)

        if self.dealer.hand.is_blackjack() or self.dealer.hand.is_bust():
            self.dealer.stand()
            self.current_turn = 0
            return

        # If the dealer has a hand value less than 17, they hit

        if self.dealer.hand.get_hand_value() < 17:
            self.dealer.hit(self.deck.deal_card())
            self.current_turn = 0
            return


    def new_game(self):
        pass
    

if __name__ == "__main__":

    # Set up the main display class and the main game class

    d = Display(1200, 700)
    game = BlackjackGame()
    
    # Constant loop to keep the game running as long as the player doesn't exit out of the window.

    while d.running:
        for event in py.event.get():      
            if event.type == py.QUIT: 
                d.running = False