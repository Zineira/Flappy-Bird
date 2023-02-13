import pygame


class Canudos:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        try:
            self.image = pygame.image.load(image)
        except Exception as e:
            print("Ocorreu um erro ao carregar a imagem:", e)
        self.image = pygame.transform.scale(self.image, (100, 500))

    def update(self):
        self.x -= 2

    def draw(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))
