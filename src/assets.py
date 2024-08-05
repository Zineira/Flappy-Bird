import pygame
from configs import *

def load_assets():
    # Carrega e redimensiona as imagens do jogo
    assets = {
        'bird_image': pygame.image.load('../public/bird.png').convert_alpha(),
        'pipe_image': pygame.image.load('../public/pipe.png').convert_alpha(),
        'background_image': pygame.image.load('../public/background.png').convert_alpha(),
    }
    assets['bird_image'] = pygame.transform.scale(assets['bird_image'], (50, 35))
    assets['pipe_image'] = pygame.transform.scale(assets['pipe_image'], (80, 500))
    assets['background_image'] = pygame.transform.scale(assets['background_image'], (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    return assets