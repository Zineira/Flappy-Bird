import pygame
import random
from configs import *

class Piping:
    def __init__(self, pipe):
        self.image = pipe
        self.inverted_image = pygame.transform.flip(pipe, False, True)
        self.pipes = []
        self.spawn_pipe()

    def spawn_pipe(self):
        
        pipe_height = random.randint(150, 400)

        top_pipe_rect = self.inverted_image.get_rect(midbottom=(SCREEN_WIDTH, pipe_height - PIPES_GAP // 2))
        bottom_pipe_rect = self.image.get_rect(midtop=(SCREEN_WIDTH, pipe_height + PIPES_GAP // 2))

        self.pipes.append((top_pipe_rect, bottom_pipe_rect))

    def update(self):
        for top_pipe, bottom_pipe in self.pipes:
            top_pipe.x -= PIPE_SPEED
            bottom_pipe.x -= PIPE_SPEED

        if self.pipes and self.pipes[0][0].right < 0:
            self.pipes.pop(0)
            self.spawn_pipe()

    def draw(self, screen):
        for top_pipe, bottom_pipe in self.pipes:
            screen.blit(self.inverted_image, top_pipe)
            screen.blit(self.image, bottom_pipe)
            
    def check_collision(self, bird_rect):
        for top_pipe, bottom_pipe in self.pipes:
            if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                return True
        return False