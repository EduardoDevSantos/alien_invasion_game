import sys
from settings import Settings
import pygame
def run_game():
    # Inicaliza o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height, ai_settings.screen_height)
        )
    pygame.display.set_caption("Alien Invasion")
    # Inicia o laço principal do jogo
    while True:
        # Observa eventosde teclado e de mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Redesenha a tela  a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)
        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()