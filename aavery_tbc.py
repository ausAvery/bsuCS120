"""
tbc.py
create the turn-based combat system
"""
import random

class Character(object):
    def __init__(self, name = "anonymous", hitPoints = 20, hitChance = 50, maxDamage = 5, armor = 0):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = value
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
        
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = value
        
    def hitMethod(self, character):
        roll = random.randrange(1, 100)
        
        if roll <= self.hitChance:
            print(f"{self.name} attacked and hit {character.name},")
            roll = random.randint(1, self.maxDamage)
            print(f"{self.name} dealt {roll} damage to {character.name}.")
            print(f"{character.name}'s armor absorbs {character.armor} points.")
            damage = roll - character.armor
            if (character.armor - damage) > 0:
                damage = 0
            else:
                character.hitPoints = (character.hitpoints + character.armor - damage)
        else:
            print(f"{self.name} attacked and missed.")                
                
    def printStats(self):
        print(f"""
            {self.__name}
            =============
            Hit Points: {self.__hitPoints}
            Hit Chance: {self.__hitChance}%
            Max Damage: {self.__maxDamage}
            Armor: {self.__armor}
        """)
        
def fightMechanism(user, character):
    keepGoing = True
    while keepGoing:
        user = hitMethod(character)
        character = hitMethod(user)
        
        if user.hitMethod <= 0:
            print(f"{character} wins!")
            keepGoing = False
        elif character.hitMethod <= 0:
            print(f"{user} wins!")
            keepGoing = False
    
        
        

# main() code for combat.py
def main():
    hero = Character()
    hero.name = "hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    
    monster = Character("monster", 50, 25, 8, 0)
    
#    hero.hitMethod(hero, "hitChance", "maxDamage")
#    monster.hitMethod(monster, "hitChance", "maxDamage")
    # probably need to call intTest() inside main()
    hero.printStats()
    monster.printStats()
    

if __name__ == "__main__":
    main()