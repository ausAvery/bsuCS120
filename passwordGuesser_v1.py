# While keepGoing Loop
# create a variable called password. Assign it value "password"
# create a sentry variable called keepGoing. Assign it value 'True'
# While keepGoing, prompt "Can you guess the password?"
# create a str variable called guess. Prompt "Enter your guess: "
# convert guess to guess.lower
# if guess is equal to "password"
#	assign 'False' to keepGoing variable
# else print "Wrong password"
# for each guess add +1 to int variable guess
# while guess is > 3 print "Wrong password."
# if guess == 3
# print "Commencing missle launch countdown"
# print "3"
# print "2"
# print "1"
# print "Missles are a go, launch launch launch!!!"

password = "password"
keepGoing = True
guessCount = str("0")

while keepGoing:
    print("Can you guess the password?")
    
    guess = input("Enter your guess: ")
    guess = guess.lower()
    if guess != "password":
        keepGoing = True
        print("Wrong, try again")
    else:
        if guess == password:
            keepGoing = False
    for i in guessCount:
        guessCount = int(guessCount)
        guessCount = (guessCount + 1)
while guessCount != 3:
    keepGoing = True
        