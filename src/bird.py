import pygame
from configs import *

class Bird:
    def __init__(self, image):
        self.original_image = image  # Armazena a imagem original
        self.image = image
        self.image = image
        self.rect = self.image.get_rect()
        self.x = 200
        self.y = SCREEN_HEIGHT//2
        self.speed = 0
    
    #bird's movement

    def flap(self):
        self.speed = STRENGTH_FLAP
        angle = -self.speed * 0.5  # Ajusta o fator de multiplicação conforme necessário
        self.image = pygame.transform.rotate(self.original_image, angle)
       
    def update(self):
        self.speed += GRAVITY
        

        # Multiplica a velocidade pelo fator de gravidade exponencial
        self.y += self.speed  # Atualiza a posição y do pássaro com base na velocidade
       
        self.rect = self.image.get_rect(center = (self.x, self.y))
        

    #draw the bird
    def draw(self, screen):
        screen.blit(self.image, self.rect)          # blint draw the image in the screen
    
    #colisions   
    def check_collision(self):
        if self.y <= 0 or self.y >= SCREEN_HEIGHT:          #limits of space
            return True
        return False