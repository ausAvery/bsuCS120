import pygame, simpleGE, random, sys

"""
    asteroids.py
    CS 120 Final
    Demonstrate the knowledge of coding
    learned over summer semester
    by Austin Avery
"""

class Game(simpleGE.Scene):
    
    def __init__(self, size = (720, 480)):
        super().__init__()
        
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.setCaption("Asteroids")
        
        self.spaceship = Spaceship(self)

        self.asteroidLg = AsteroidLg(self)
        
        self.asteroidSm = AsteroidSm(self)
        
#         self.bullet = Bullet(self, self.spaceship)

        #what i think bullet will become
        self.bullet = 0
        self.bullets = []
        self.numBullets = 100
        for i in range(self.numBullets):
            self.bullets.append(Bullet(self, self.spaceship))
        
        self.sprites = [self.spaceship,
                        self.asteroidLg,
                        self.asteroidSm,
                        self.bullets]
        
    def processEvent(self, event):
        
        if self.isKeyPressed(pygame.K_SPACE):
            self.bullet += 1
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
    def process(self):
        if self.isKeyPressed(pygame.K_s):
            self.bullet += 1
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
        
class Spaceship(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("spaceship.png")
        self.position = (360, 240)
        self.setSize(50,30)
        self.imageAngle = 90
        self.drag = .05
        self.accel = .2

    def process(self):
        
        # motion for spaceship
        if self.isKeyPressed(pygame.K_LEFT):
            self.imageAngle += 5
        if self.isKeyPressed(pygame.K_RIGHT):
            self.imageAngle -= 5
        if self.isKeyPressed(pygame.K_UP):
            self.addForce(self.accel, self.imageAngle)
            
        # bullet shooting mechanism
#         if self.isKeyPressed(pygame.K_SPACE):

        # compensate for drag (DOES NOT WORK)
#         self.speed *= (1 - self.drag)
            

class AsteroidLg(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("asteroidLg.png")
        self.setSize(100, 80)
        self.reset()
    
    def reset(self):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.position = (x, y)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
    
#     def checkBounds(self):

class AsteroidSm(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("asteroidSm.png")
        self.setSize(60, 40)
        self.reset()
        self.hide()
    
    def reset(self):
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.position = (x, y)
        self.dx = random.randint(-3, 8)
        self.dy = random.randint(-5, 5)
        
class Bullet(simpleGE.Sprite):
    
    def __init__(self, scene, parent):
        super().__init__(scene)
        self.parent = parent
        
#         self.setImage("bullet.png")
#         self.setSize(100, 100)
        self.colorRect("sky blue", (8,3))
        self.boundAction = self.HIDE
#         self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
#         if not self.visible:
        self.show()
        self.position = self.parent.position
        self.imageAngle = self.parent.imageAngle
        self.moveAngle = self.parent.imageAngle
        self.speed = 15        
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
    
    # helps close pygame window
    sys.exit()
    pygame.quit()