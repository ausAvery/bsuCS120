# Austin Avery
# Friday May 17, 2024
# Knock Knock Joke

# Obtain fName
fName = input("What is your name? ")

# Obtain greeting answer
greeting = input(f"Hi {fName}, do you want to hear a knock knock joke? (Y/N): ")

# Additional variables
whosThere = "Who's there?"
artWho = "Art who?"

# Start Knock Knock Joke
if greeting.startswith("Y"):
    print("Knock knock")
    answer = input("")
    if answer == ("Who's there?"):
        print("Art")
        answer2 = input("")
        if answer2 == "Art who?":
            print("R2-D2, who else?")
        if answer2 == "art who?":
            print("R2-D2, who else?")
        else:
            print(f"You're supposed to say '{artWho}'")
    if answer == "who's there?":
        print("Art")
        answer2 = input("")
        if answer2 == "Art who?":
            print("R2-D2, who else?")
        if answer2 == "art who?":
            print("R2-D2, who else?")
        else:
            print(f"You're supposed to say '{artWho}'")
    else:
        print(f"You're supposed to say '{whosThere}'.")
if greeting.startswith("y"):
    print("Knock knock")
    answer = input("")
    if answer == ("Who's there?"):
        print("Art")
    if answer == ("who's there?"):
        print("Art")
        answer2 = input("")
        if answer2 == ("Art who?"):
            print("R2-D2, who else?")
        if answer2 == ("art who?"):
            print("R2-D2, who else?")
        else:
            print(f"You're supposed to say '{artWho}'")
    else:
        print(f"You're supposed to say '{whosThere}'.")
else:
    print("Oh, I'm sorry to hear that. It was going to be really funny")