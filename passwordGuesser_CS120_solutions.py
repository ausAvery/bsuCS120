# Password guessing machine
# 3 problematic solutions

"""

# Problematic solution #1

correct = "password"
tries = 0
guess = ()

while ((guess != correct) and (tries < 3)):
    guess = input("Password: ")
    if guess == correct:
        print("Good job guessing the password!")
    else:
        tries += 1
        if tries == 3:
            print("Commencing missle launch")
            print("3...")
            print("2..")
            print("1.")
            print("Missles are a go, Launch Launch Launch!")

"""
"""
# Problematic Solution #2

correct = "password"
tries = 0

while (True):
    guess = input("Password: ")
    tries += 1
    if guess == correct:
        print("Good job.")
        break
    if tries > 3:
        print("Commencing missle launch")
        print("3...")
        print("2..")
        print("1.")
        print("Missles are a go, Launch Launch Launch!")
        break
"""
"""
# Problematic Solution #3 (worst one yet)

correct = "password"
tries = 0

while tries < 3:
    guess = input("Password: ")
    tries += 1
    if guess == correct:
        tries = 3
"""
"""
# My version of Solution #3

correct = "password"
tries = 0

while tries != 3:
    guess = input("Password: ")
    tries += 1
    if guess == correct:
        tries = 3
    if tries < 3:
        print("Wrong, try again.")
if tries == 3: # do not make this a 'while' statement, it will print indefinitely
    print("Missle launch is go!")
"""

# keepGoing to the rescue

correct = "password"
tries = 0
keepGoing = True
while keepGoing:
    tries += 1
    guess = input("Password: ")
    if guess == correct:
        print("Good job.")
        keepGoing = False
    if tries >= 3:
        print("You lose.")
        keepGoing = False