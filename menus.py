import pygame
from main import *

def main_menu(screen):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        font = pygame.font.Font(None, 74)
        text = font.render('Asteroids', True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        screen.blit(text, text_rect)

        play_font = pygame.font.Font(None, 50)
        play_text = play_font.render('Play Game', True, (255, 255, 255))
        play_text_rect = play_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
        mouse_pos = pygame.mouse.get_pos()
        if play_text_rect.collidepoint(mouse_pos):
            play_text = play_font.render('Play Game', True, (128, 128, 128))
        else:
            play_text = play_font.render('Play Game', True, (255, 255, 255))

        if play_text_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            game_loop(screen)
        
        screen.blit(play_text, play_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

def ingame_menu(screen):
    paused = True

    while paused:

        font = pygame.font.Font(None, 74)
        text = font.render('Paused', True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(text, text_rect)

        resume_font = pygame.font.Font(None, 50)
        resume_text = resume_font.render('Resume Game', True, (255, 255, 255))
        resume_text_rect = resume_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))

        mouse_pos = pygame.mouse.get_pos()

        if resume_text_rect.collidepoint(mouse_pos):
            resume_text = resume_font.render('Resume Game', True, (128, 128, 128))
        else:
            resume_text = resume_font.render('Resume Game', True, (255, 255, 255))

        if resume_text_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            paused = False
        
        screen.blit(resume_text, resume_text_rect)

        quit_text = resume_font.render('Quit Game', True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200))

        if quit_text_rect.collidepoint(mouse_pos):
            quit_text = resume_font.render('Quit Game', True, (128, 128, 128))
        else:
            quit_text = resume_font.render('Quit Game', True, (255, 255, 255))

        if quit_text_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            paused = False
            main_menu(screen)

        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if event.key == pygame.K_ESCAPE:
                        paused = False

def game_over():
    pass

def config():
    pass