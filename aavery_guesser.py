# Austin Avery
# Tuesday, 21 May 2024
# Number Guesser

import random

attempts = 0
keepGoing = True
correct = random.randint(1,100)
#print(correct) # for testing purposes
print("***  INSTRUCTIONS    ***")
print("The computer will think of a number between 1-100.")
print("It is your job to guess it correctly.")
print("Good luck!:)")

while keepGoing:
    attempts += 1
    guess = input(f"Attempt {attempts}, please guess a number: ")
    if guess.isalpha():
        print("You must enter a number, that's going to cost you an attempt.")
    else:
        guess = int(guess)
        if guess < correct:
            print("Too low.")
        elif guess > correct:
            print("Too high.")
        elif guess == correct:
            print(f"Congratulations! {guess} was correct!")
            keepGoing = False
        else:
            if attempts >= 7:
                print("You should be able to get this in 7 attempts. Try again.")
                keepGoing = False
