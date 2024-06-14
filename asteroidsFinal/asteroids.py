import pygame, simpleGE, random, sys

"""
    asteroids.py
    CS 120 Final
    Demonstrate the knowledge of coding
    learned over summer semester
    by Austin Avery
"""

class StartMenu(simpleGE.Scene):
    
    def __init__(self, size = (720, 480)):
        super().__init__()
        
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.setCaption("Asteroids --Start Menu--")
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
            "Use the UP arrow to accelerate.",
            "Use the Left & Right arrows to rotate your ship.",
            "Use the SPACEBAR to shoot.",
            "Shoot the asteroids to destroy them...",
            "Dodge them at all costs to stay alive.",
            "Good luck! :)"
            ]
        self.instructions.center = (360, 180)
        self.instructions.size = (500, 200)
        
        self.sprites = [self.instructions]

class Game(simpleGE.Scene):
    
    def __init__(self, size = (720, 480)):
        super().__init__()
        
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.setCaption("Asteroids")
        
        self.lblScore = LblScore()
        self.score = 0
        
        self.lblLives = LblLives()
        self.lives = 5
        
        self.spaceship = Spaceship(self)

#         self.asteroidLg = AsteroidLg(self)
        self.lgAsteroids = []
        self.numLgAsteroids = 3
        for i in range(self.numLgAsteroids):
            self.lgAsteroids.append(AsteroidLg(self))
        
        self.asteroidSm = AsteroidSm(self)
        
#         self.bullet = Bullet(self, self.spaceship)

        #what i think bullet will become
        self.bullet = 0
        self.bullets = []
        self.numBullets = 100
        for i in range(self.numBullets):
            self.bullets.append(Bullet(self, self.spaceship))
        
        self.sprites = [self.spaceship,
                        self.lgAsteroids,
                        self.asteroidSm,
                        self.bullets,
                        self.lblScore,
                        self.lblLives]
        
    def processEvent(self, event):
        
        """ shoot bullet from spaceship """
        if self.isKeyPressed(pygame.K_SPACE):
            self.bullet += 1
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
    def process(self):
        
        """ easter egg """
        if self.isKeyPressed(pygame.K_s):
            self.bullet += 1
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
        """ check for collision between bullet and asteroid """
        for asteroid in self.lgAsteroids:
            if self.bullets[self.bullet].collidesWith(asteroid):
                self.bullets[self.bullet].reset()
                asteroid.reset()
                self.score += 50
                self.lblScore.text = f"Score: {self.score}"
            if asteroid.collidesWith(self.spaceship):
                asteroid.reset()
                self.lives -= 1
                self.lblLives.text = f"Lives: {self.lives}"
                if self.lives == 0:
                    self.stop()

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
        self.dx = random.randint(-4, 4)
        self.dy = random.randint(-4, 4)

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
    
    def reset(self):
        self.boundAction = self.HIDE
        self.hide()

class LblScore(simpleGE.Label):
    
    def __init__(self):
        super().__init__()
        
        self.center = (360, 30)
        self.clearBack = True
        self.text = "Score: 0"
        
class LblLives(simpleGE.Label):
    
    def __init__(self):
        super().__init__()
        
        self.center = (50, 30)
        self.clearBack = True
        self.text = "Lives: 5"
        
        """ use spaceship sprite as lives??? """
#         self.lives = Spaceship(self)        
#         self.livesRemaining = []
        
#         for i in range(self.numLives):
#             self.livesRemaining += 1
#                 if self.livesRemaining >= 5:
#                     self.stop()
        
def main():
    startMenu = StartMenu()
    startMenu.start()
    
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
    
    # helps close pygame window
    sys.exit()
    pygame.quit()