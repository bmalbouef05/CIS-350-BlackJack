import pygame as py

class Display():
    def __init__(self, width, height):
        bg_color = (41, 196, 18)
        self.screen = py.display.set_mode((1200, 700))
        py.display.set_caption('BlackJack')
        self.screen.fill(bg_color)
        py.display.flip()
        self.running = True

