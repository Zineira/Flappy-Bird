import pygame
import bird
import Menu
import canudos
import random

pygame.init()

clock = pygame.time.Clock()

passaro = bird.Bird(200, 300, "paxaro.png")
cano = canudos.Canudos(1150, 550, "cano1.png", "cano2.png")

screen_height = 760
screen_width = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
background_imagem = pygame.image.load("background.png")
screen.blit(background_imagem, (0, 0))

# Instancia o objeto Menu
menu = Menu.Menu(screen)

# Variável para controlar se o menu está sendo exibido ou não
showing_menu = True

# Loop principal do jogo
running = True
while running:
    # Verifica os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Verifica se o mouse foi clicado
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()

            # Verifica se a opção "Play" foi selecionada
            if menu.check_play_selected(mouse_pos):
                showing_menu = False

            # Verifica se a opção "Sair" foi selecionada
            elif menu.check_quit_selected(mouse_pos):
                running = False

    # Desenha o menu ou o jogo na tela
    if showing_menu:
        menu.show_menu()
    else:
        # Update game logic and display here
        background_imagem = pygame.image.load("background.png")
        screen.blit(background_imagem, (0, 0))
        cano.update()
        cano.draw(screen)
        passaro.update(0.80)
        passaro.draw(screen)

    pygame.display.update()
    clock.tick(60)
