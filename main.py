import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main_menu():
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
            game_loop()
        
        screen.blit(play_text, play_text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

def ingame_menu():
    pass

def game_over():
    pass

def config():
    pass

def init():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
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
 
    
    while True:
        pygame.Surface.fill(screen, (0, 0, 0))

        for object in drawable:
            object.draw(screen)
        for object in updateable:
            object.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split(dt)
                    shot.kill()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        clock.tick(60)

        dt = clock.tick(60) / 1000

        
def main():
    init()
    main_menu()
        
    

if __name__ == "__main__":
    main()
