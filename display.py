import pygame as py

class Display():
    def __init__(self, width, height):
        self.bg_color = (41, 196, 18)
        self.screen = py.display.set_mode((1200, 700))
        py.display.set_caption('BlackJack')
        self.screen.fill(self.bg_color)
        py.draw.rect(self.screen, (155, 155, 155), py.Rect(900, 0, 300, 700))
        py.display.flip()
        self.running = True

    def reset_screen(self):
        self.screen.fill(self.bg_color)
        py.display.flip()
        py.draw.rect(self.screen, (155, 155, 155), py.Rect(900, 0, 300, 700))
        

