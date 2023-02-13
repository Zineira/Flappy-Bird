import pygame


class Menu:
    def __init__(self, screen, test2):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Configurações do texto do menu
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 48)

        # Prepara a imagem do título
        self.prep_title("Flappy Bird")

        # Prepara as opções do menu
        self.prep_options()

    def prep_title(self, title):
        """Transforma o título em uma imagem renderizada e centraliza-o na tela"""
        self.title_image = self.font.render(
            title, True, self.text_color, (0, 0, 0))
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.centerx = self.screen_rect.centerx
        self.title_image_rect.top = self.screen_rect.top + 50

    def prep_options(self):
        """Cria as imagens das opções do menu e centraliza-as na tela"""
        self.play_image = self.font.render(
            "Play", True, self.text_color, (0, 0, 0))
        self.play_image_rect = self.play_image.get_rect()
        self.play_image_rect.centerx = self.screen_rect.centerx
        self.play_image_rect.top = self.title_image_rect.bottom + 50

        self.quit_image = self.font.render(
            "Sair", True, self.text_color, (0, 0, 0))
        self.quit_image_rect = self.quit_image.get_rect()
        self.quit_image_rect.centerx = self.screen_rect.centerx
        self.quit_image_rect.top = self.play_image_rect.bottom + 20

    def show_menu(self):
        """Desenha o título e as opções do menu na tela"""
        self.screen.blit(self.title_image, self.title_image_rect)
        self.screen.blit(self.play_image, self.play_image_rect)
        self.screen.blit(self.quit_image, self.quit_image_rect)

    def check_play_selected(self, mouse_pos):
        """Verifica se o jogador clicou na opção "Play" e retorna True se sim"""
        if self.play_image_rect.collidepoint(mouse_pos):
            return True
        return False

    def check_quit_selected(self, mouse_pos):
        """Verifica se o jogador clicou na opção "Sair" e retorna True se sim"""
        if self.quit_image_rect.collidepoint(mouse_pos):
            return True
        return False
