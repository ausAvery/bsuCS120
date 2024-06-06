"""
    bobWeave.py
    Demonstrates sprite movement and collision
    Austin Avery
"""
import simpleGE, pygame, random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("lavaOcean.jpg")
        
        self.avatar = Avatar(self)
        
        self.axes = []
        self.numAxes = 10
        self.sndAxe = simpleGE.Sound("axe.wav")
        
        for i in range(self.numAxes):
            self.axes.append(Axe(self))
        
        self.sprites = [self.avatar,
                        self.axes]
    
    def process(self):
        for axe in self.axes:
            if axe.collidesWith(self.avatar):
                axe.reset()
                self.sndAxe.play()

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
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
    pygame.quit()