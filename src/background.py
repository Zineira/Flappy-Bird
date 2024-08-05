import pygame
from configs import  *

class Background:
    def __init__(self, image):
        self.image = image
        self.x1 = 0
        self.x2 = SCREEN_WIDTH

    def update(self):
        #background movement
        self.x1 -= BACKGROUND_SPEED
        self.x2 -= BACKGROUND_SPEED
        
        if self.x1 <= -SCREEN_WIDTH:                # when first plane leaves the screen then it resets and 
            self.x1 = self.x2 + SCREEN_WIDTH        # starts on the end of the screen
        if self.x2 <= -SCREEN_WIDTH:
            self.x2 = self.x1 + SCREEN_WIDTH
          

    def draw(self, screen):
        # Desenha as duas imagens de fundo na tela
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))