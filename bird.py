import pygame


class Bird:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.salto = -10
        self.g = 1
        try:
            self.image = pygame.image.load(image)
        except Exception as e:
            print("Ocorreu um erro ao carregar a imagem:", e)
        self.image = pygame.transform.scale(self.image, (60, 50))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jump()
        self.y += self.salto
        self.salto += self.g * dt
        if self.y >= 650:
            self.salto = 0
        if self.y <= 0:
            self.y = 0

    def jump(self):
        self.salto = -10

    def draw(self, screen):
        screen.blit(self.image, (int(self.x), int(self.y)))
