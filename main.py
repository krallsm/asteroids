import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
                sys.exit()

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

def init():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

def game_loop(screen):
    clock = pygame.time.Clock()
    dt = 0
    running = True
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()
    
    font = pygame.font.Font(None, 36)
    
    while running:
        pygame.Surface.fill(screen, (0, 0, 0))

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            ingame_menu(screen)

        for object in drawable:
            object.draw(screen)
        for object in updateable:
            object.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                running = False
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split(dt)
                    shot.kill()
                    player.score += 10

        score_text = font.render(f'Score: {player.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        clock.tick(60)

        dt = clock.tick(60) / 1000
       
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    init()
    main_menu(screen)

if __name__ == "__main__":
    main()
