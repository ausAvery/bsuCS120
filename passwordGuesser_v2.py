# Second attempt of passwordGuess after watching video
# My own twist, start with 3 attempts, after each attempt subtract 1, once attempts hit 0, fail
# This version is fun:)
# Hint: Most basic password 

correct = "password"
attempts = 3
keepGoing = True

while keepGoing:
    guess = input(f"Password (you have {attempts} attempts left): ")
    attempts -= 1
    if guess == correct:
        keepGoing = False
        print("Login successful.")
    if attempts == 0:
        keepGoing = False
        print("You have failed three times. Commencing missle launch in...")
        print("3")
        print("2")
        print("1")
        print("Launch! Launch! Launch!")