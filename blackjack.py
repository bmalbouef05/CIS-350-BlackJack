import random
import pygame
from display import Display
from deck import Deck
from player import Player
from button import Button


class BlackjackGame:
    def __init__(self):

        # Initialize the Deck and both the Player and Dealer classes

        self.deck = Deck()
        self.player = Player(True)
        self.dealer = Player(False)

        self.money_total = 1000
        self.rounds_total = 0
        
        # Variable to keep track of whether or not the game is being played
        self.play_game = True
        
        # self.init_ui()
        pygame.init()
        self.new_game()
    
    def deal_start_cards(self):
        
        # Make a new deck

        self.deck.reset_deck()

        # Draws two cards per player to start off

        self.player.hand.draw_card(self.deck.deal_card())
        self.player.hand.draw_card(self.deck.deal_card())
        self.dealer.hand.draw_card(self.deck.deal_card())
        self.dealer.hand.draw_card(self.deck.deal_card())

    def player_turn(self):

        # Needs to be implemented

        pass


    def dealer_turn(self):
        
        # If the dealer has either blackjack or bust, they "stand" (don't take any more turns)

        if self.dealer.hand.is_blackjack() or self.dealer.hand.is_bust():
            self.dealer.stand()
            return

        # If the dealer has a hand value less than 17, they hit

        if self.dealer.hand.get_hand_value() < 17:
            self.dealer.hit(self.deck.deal_card())
            return


    def new_game(self):
        pass
    

if __name__ == "__main__":

    # Set up the main display class and the main game class

    d = Display(1200, 700)
    game = BlackjackGame()

    # Setting up hit and stand button for the GUI

    hit_button = Button("Hit", 900, 500, 150, 75, d)
    stand_button = Button("Stand", 900, 400, 150, 75, d)

    # Constant loop to keep the game running as long as the player doesn't exit out of the window.

    while d.running and game.play_game:

        # Player continues to hit until they stand. Then dealer does their turns.
        
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                d.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hit_button.check_hovering():
                    print("hit")
                elif stand_button.check_hovering():
                    print("stand")