import pygame, simpleGE, random, sys

"""
    asteroids.py
    CS 120 Final
    Demonstrate the knowledge of coding
    learned over summer semester
    by Austin Avery
"""

class StartMenu(simpleGE.Scene):
    
    def __init__(self, score, size = (720, 480)):
        super().__init__()
        
        self.screen = pygame.display.set_mode(size)
        self.background = pygame.Surface(self.screen.get_size())
        self.setCaption("--Start Menu--")
        
        self.response = "Quit"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.center = (360, 180)
        self.instructions.size = (500, 200)
        self.instructions.textLines = [
            "Use the UP arrow to engage thrusters.",
            "Use the Left & Right arrows to rotate your ship.",
            "Use the SPACEBAR to shoot.",
            "Shoot the asteroids to destroy them...",
            "dodge them at all costs to stay alive.",
            "Good luck! :)"
            ]
        
        self.lblScore = simpleGE.Label()
        self.lblScore.center = (360, 350)
#         self.lblScore.bgColor = "white"
#         self.lblScore.fgColor = "black"
        self.lblScore.size = (300, 30)
        self.score = score
        self.lblScore.text = f"Previous Score: {self.score}"
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.center = (100, 400)
        self.btnPlay.text = "Play"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.center = (620, 400)
        self.btnQuit.text = "Quit"
        
        self.sprites = [self.instructions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
    def process(self):
        
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()
        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()

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

        self.lgAsteroids = []
        self.numLgAsteroids = 4
        for i in range(self.numLgAsteroids):
            self.lgAsteroids.append(AsteroidLg(self))
        
        self.asteroidSm = AsteroidSm(self)
        
        self.sndLaser = simpleGE.Sound("laser.ogg")
        self.sndExplosion = simpleGE.Sound("explosion.ogg")
        self.sndCrash = simpleGE.Sound("crash.ogg")

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
            self.sndLaser.play()
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
    def process(self):
        
        """ easter egg """
        if self.isKeyPressed(pygame.K_s):
            self.bullet += 1
            self.sndLaser.play()
            if self.bullet >= self.numBullets:
                self.bullet = 0
            self.bullets[self.bullet].fire()
            
        """ check for collisions """
        for asteroid in self.lgAsteroids:
            for bullet in self.bullets:
                if bullet.collidesWith(asteroid):
                    self.bullets[self.bullet].reset()
                    self.sndExplosion.play()
                    asteroid.reset()
                    self.score += 50
                    self.lblScore.text = f"Score: {self.score}"
                if asteroid.collidesWith(self.spaceship):
                    asteroid.reset()
                    self.sndCrash.play()
                    self.lives -= 1
                    self.lblLives.text = f"Lives: {self.lives}"
                    if self.lives == 0:
                        self.stop()

class Spaceship(simpleGE.Sprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("spaceship.png")
        self.position = (360, 240)
        self.setSize(30, 40)
        self.imageAngle = 90
        self.drag = .05
        self.accel = .2

    def process(self):
        
        """ motion for spaceship """
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
        
        """ prevent asteroid from spawning on spaceship """
        self.center = (360, 240)
        
        if self.distanceTo(self.center) <= 100:
            self.reset()
    
    def reset(self):
        
        """ spawn asteroid """
        x = random.randint(0, self.screen.get_width())
        y = random.randint(0, self.screen.get_height())
        self.position = (x, y)
        self.minSpeed = -4
        self.maxSpeed = 4
        self.speed = random.randint(self.minSpeed, self.maxSpeed)
        self.moveAngle = random.randint(1, 359)
    
    def process(self):
        
        """ prevent non-moving asteroid """
        if self.speed == 0:
            self.reset()

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
        
        self.colorRect("sky blue", (8,3))
        self.boundAction = self.HIDE
        self.hide()
        
    def fire(self):
        
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
        
#         """ use spaceship sprite as lives??? """
#         self.lives = Spaceship(self)        
#         self.livesRemaining = []
        
#         for i in range(self.numLives):
#             self.livesRemaining += 1
#                 if self.livesRemaining >= 5:
#                     self.stop()
        
def main():
    
    keepGoing = True
    score = 0
    
    while keepGoing:
        startMenu = StartMenu(score)
        startMenu.start()
        
        if startMenu.response == "Play":
            game = Game()
            game.start()
            score = game.score
        else:
            if startMenu.response == "Quit":
                startMenu.stop()
                keepGoing = False

if __name__ == "__main__":
    main()
    
    # helps close pygame window
    sys.exit()
    pygame.quit()