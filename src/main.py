import pygame
from configs import *
import utils
from assets import load_assets
from bird import Bird
from background import Background
from pipe import Piping

if __name__ == "__main__":
    #starts PyGame and set the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")
    clock = pygame.time.Clock()
    
    assets = load_assets()
    #start the assets
    
    bird = Bird(assets['bird_image'])
    pipe = Piping(assets['pipe_image'])
    background = Background(assets['background_image'])
    
    #Scores
    
    # Main Loop
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Ends the game
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # main event
                bird.flap()

        
        #Render the background
        background.update()
        background.draw(screen)
        # Render Bird
        bird.update()
        bird.draw(screen)
        # Render Pipe
        pipe.update()
        pipe.draw(screen)
        
        if bird.check_collision() or pipe.check_collision(bird.rect): 
            running = False
        
        
        pygame.display.flip()

        clock.tick(FPS)  # limits FPS to 60

    pygame.quit()

    