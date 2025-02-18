import pygame

class Button:
    def __init__(self, text, x, y, width, height, display):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.display = display
        self.clicked = False

        smallfont = pygame.font.SysFont('Corbel',35) 
  
        txt = smallfont.render(self.text, True , (0, 0, 0)) 

        pygame.draw.rect(self.display.screen, (170, 170, 170), [self.x, self.y, self.width, self.height])
        display.screen.blit(txt, [self.x + (self.width/3), self.y + (self.height/3)])
        pygame.display.update()

    def check_hovering(self):
        mouse = pygame.mouse.get_pos()

        if (self.x <= mouse[0] <= self.x + self.width) and (self.y <= mouse[1] <= self.y + self.height):
            return True

    def is_clicked(self):
        return self.clicked



    