"""
Created on Sun Jun  2 00:33:01 2024

@author: aavery
"""

def main():
    
    # I - Import & Initialize
    import pygame
    pygame.init()
    
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello, world!")
    
    # E - Entities (just a background for now)
    background = pygame.Surface(screen.get_size())
    background.fill(pygame.Color("cornflowerblue"))
    
    # A - Action broke into A.L.T.E.R
    
        # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    
        # L - Set up main Loop
    while keepGoing:
        
        # T - Timer to set frame rate
        clock.tick(30)
        
        # E - Event-handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        # R - Refresh display
        screen.blit(background, (0,0))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
    