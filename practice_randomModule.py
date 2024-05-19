# demonstrating features of random library, first import the random module

import random



# use randint to create random value within a range
dieRoll = random.randint(1,6)
print(dieRoll)

print()



# using random in a loop that happens 10 times
for i in range(10):
    dieRoll = random.randint(1,6)
    print(f"You rolled a {dieRoll}.")
    
print()



# let's say you have a hand of cards
cards = ["Ace of Spades", "Jack of Clubs", "King of Hearts", "Four of Diamonds"]

# use the len function to calculate how many cards are in the list
numCards = len(cards)

# randRange lets you get a legal index from a list, normally gives a 0 - n-1 value like the range operator
cardNum = random.randrange(numCards)
print(f"You rolled a {cardNum}.")
print(f"That's a {cards[cardNum]}.")



# we can feed a number to the seed function, or a string (which will be converted to a number)
random.seed("CS 120")

# now produce some random numbers
for i in range(10):
    print(random.randint(1,10), end = " ")
print()

# try it again and you'll get a new set of random numbers
for i in range(10):
    print(random.randint(1,10), end = " ")
print()

# reset the seed and you'll get the same sequence again
random.seed("CS 120")

for i in range(10):
    print(random.randint(1,10), end = " ")
print()

















