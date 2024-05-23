""" cards.py
    demonstrates functions
    manage a deck of cards db

"""

import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)

def initCards():
    """
    Parameters: n/a
	Create list named cardDB
	Assign initial value zero for every element in list of 52
	Return cardDB
    """
    
    cardDB = [DECK] * NUMCARDS
    return cardDB

def showDB(cardDB):
    """
    Parameters: cardDB
	Step through all the cards
	Print card number
	Print card name
	Print card location
	No return
    """
    
    for cardNum, location in enumerate(cardDB):
        print(f"{cardNum:3}: {getCardName(cardNum):20} {HANDS[location]}")

def getCardName(cardNum):
    """
    parameters: cardNum
	integer divide cardNum by 13 -> suit
	modulus of cardNum and 13 -> rank
	use SUITNAME & RANKNAME tuples to get a string name
	return card name
    """
    
    suit = cardNum // 13
    rank = cardNum % 13
    cardName = (f"{RANKNAME[rank]} of {SUITNAME[suit]}")
    
    return cardName
    
def assignCard(cardDB, hand):
    """
    parameters: cardDB, hand
	pick a random number 0-51
	assign hand to that number’s location
	(how do we make sure same card isn’t chosen twice?)
	add a while loop to check if card has been assigned a location
	No return value
    """ 
    
    cardNum = random.randrange(NUMCARDS)
    while cardDB[cardNum] != DECK:
        cardNum = random.randrange(NUMCARDS)
    cardDB[cardNum] = hand
    
def showHand(cardDB, hand):
    """
    parameters: cardDB, hand
	step through all cards
		if card is in the hand
			print card name
	No return value
    """
    print()
    
    print(f"Cards in {HANDS[hand]}'s hand:")
    
    for cardNum, location in enumerate(cardDB):
        if location == hand:
            print(f"{getCardName(cardNum)}")
            
    print()

main()
