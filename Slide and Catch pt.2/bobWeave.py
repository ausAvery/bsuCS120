import pygame, simpleGE, random, sys

"""
    bobWeave.py
    Demonstrates sprite movement and collision
    Austin Avery
"""

# NOTE: Default screen size is 640 by 480

class Intro(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        
        self.setImage("lavaOcean.jpg")
        self.response = "Quit"
        
        self.lblInstructions = simpleGE.MultiLabel()
        self.lblInstructions.textLines = [
            "You are Joe the adventurer",
            "Move Joe using the W,A,S,D keys",
            "Avoid the falling Axes at all costs",
            "and survive as long as possible",
            "",
            "Good luck! :)"]
        self.lblInstructions.center = (320, 200)
        self.lblInstructions.size = (400, 250)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 420)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (540, 420)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: 0"
        self.lblScore.center = (320, 420)  
        
        self.sprites = [self.lblInstructions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
        def processEvent(self):
            if self.btnPlay.clicked:
                self.response = "Play"
                self.stop()
        
            if self.btnQuit.clicked:
                self.response = "Quit"
                self.stop()      

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("lavaOcean.jpg")
        
        self.lblScore = LblScore()
        
        self.lblTimer = LblTimer()
        
        self.lblLives = LblLives()
        self.lives = 5
        
        self.avatar = Avatar(self)
        
        self.axes = []
        self.numAxes = 10
        self.sndAxe = simpleGE.Sound("axe.wav")
        
        for i in range(self.numAxes):
            self.axes.append(Axe(self))
        
        self.sprites = [self.avatar,
                        self.axes,
                        self.lblScore,
                        self.lblTimer,
                        self.lblLives]
    
    def process(self):
        for axe in self.axes:
            if axe.collidesWith(self.avatar):
                axe.reset()
                self.sndAxe.play()
                self.lives -= 1
                self.lblLives.text = f"Lives: {self.lives}"
            if self.lives == 0:
                self.stop()

class Avatar(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("avatar.png")
        self.setSize(50, 50)
        self.position = (320,240)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_w):
            self.y -= self.moveSpeed
        if self.isKeyPressed(pygame.K_a):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_s):
            self.y += self.moveSpeed
        if self.isKeyPressed(pygame.K_d):
            self.x += self.moveSpeed

class Axe(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("axeDouble.png")
        self.setSize(50, 50)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = (random.randint(0, self.screenWidth))
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
    
    def checkBounds(self):
        if self.y > self.screenHeight:
            self.reset()
            
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        
        #self.clearBack = True
        self.bgColor = "yellow"
        self.fgColor = "black"
        self.center = (320, 30)
        self.score = simpleGE.Timer()
        
    def process(self):
        self.text = f"Score: {self.score.getElapsedTime():.0f}"
        
class LblTimer(simpleGE.Label):
    def __init__(self):
        super().__init__()
        
        self.bgColor = "yellow"
        self.fgColor = "black"
        self.center = (560, 30)
        self.timer = simpleGE.Timer()
        
    def process(self):
        self.text = f"{self.timer.getElapsedTime():.2f}"
        
class LblLives(simpleGE.Label):
    def __init__(self):
        super().__init__()
        
        self.bgColor = "yellow"
        self.fgColor = "black"
        self.center = (80, 30)
        self.text = "Lives: 5"
        
def main():
    keepGoing = True
    game = Game()
    game.start()

    while keepGoing:
        intro = Intro()
        intro.start()
        if intro.response == "Play":    
            game = Game()
            game.start()
        else:
            keepGoing = False

if __name__ == "__main__":
    main()
    
    # helps close pygame window
    sys.exit()
    pygame.quit()