import pygame
from bird import Bird

pygame.init()

passaro = Bird(200, 300, "paxaro.png")

screen_height = 1000
screen_width = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic and display here
    # ...
    screen.fill((255, 255, 255))  # Preenche a tela com branco
    passaro.update(0.50)
    passaro.draw(screen)
    pygame.display.update()
