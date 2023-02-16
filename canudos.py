import pygame
import random


class Canudos:
    def __init__(self, x, height, image_top, image_bottom):
        self.x = x
        self.y = random.randint(-430, -130)
        self.height = height
        self.gap = 100
        try:
            self.image_top = pygame.image.load(image_top)
            self.image_bottom = pygame.image.load(image_bottom)
        except Exception as e:
            print("Ocorreu um erro ao carregar a imagem:", e)
        self.image_top = pygame.transform.scale(self.image_top, (125, 500))
        self.image_bottom = pygame.transform.scale(
            self.image_bottom, (125, 500))

    def update(self):
        self.x -= 5

    def draw(self, screen):
        print(self.y)
        screen.blit(self.image_top, (int(self.x), self.y))
        screen.blit(self.image_bottom,
                    (int(self.x), int(self.y+self.height+self.gap)))
