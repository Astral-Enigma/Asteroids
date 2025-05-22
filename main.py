import pygame
from constants import *
from player import *

'''
GAME LOOP
'''

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    new_player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen,"black")
        new_player.draw(screen)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.get_time()
        dt = dt/1000

        new_player.update(dt)

'''
End of file stuff
'''

if __name__ == "__main__":
    main()
