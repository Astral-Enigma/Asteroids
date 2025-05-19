import pygame
from constants import *

'''
GAME LOOP
'''

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen,"black")
        pygame.display.flip()

'''
End of file stuff
'''

if __name__ == "__main__":
    main()
