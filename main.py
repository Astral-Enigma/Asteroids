import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from Shots import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    new_player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)


    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable)

#GAME LOOP

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen,"black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.get_time()
        dt = dt/1000

        updatable.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision_check(new_player) == True:
                print("Game Over")
                pygame.quit()
                return
        
        for asteroid in asteroid_group:
            for shot in shots_group:
                if asteroid.collision_check(shot) == True:
                    asteroid.split()
                    shot.kill() 


'''
End of file stuff
'''

if __name__ == "__main__":
    main()
