import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from menus import *

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
