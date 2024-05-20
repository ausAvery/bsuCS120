# Knock Knock (working version)
# Austin Avery
# Monday May 20, 2024 0402

# List of variables - first variable asks user if they want to hear a knock knock joke
answer = input("Do you want to hear a knock knock joke? (Y/N): ")
whosThere = ("Who's there?")
artWho = ("Art who?")
knock = ("Knock knock" )
art = ("Art")
r2d2 = ("R2-D2, who else?")
noFun = ("You're no fun")

# print(f"You're supposed to say '{whosThere}'")
# print(f"You're supposed to say '{artWho}'")

# Start 'if' structure using the beginning character of variable 'answer'
# if answer begins with a "y" begin the knock knock joke otherwise go to 'else' statement
if answer.startswith("y"):
    print(knock)
    answer2 = input("")
    if answer2 == "who's there?":
        print(art)
        answer3 = input("")
        if answer3 == "art who?":
            print(r2d2)
        else:
            if answer3 == "Art who?":
                print(r2d2)
            else:
                print(f"You're supposed to say '{artWho}'")
    else:
        if answer2 == "Who's there?":
            print(art)
            answer3 = input("")
            if answer3 == "art who?":
                print(r2d2)
            else:
                if answer3 == "Art who?":
                    print(r2d2)
                else:
                    print(f"You're supposed to say '{artWho}'")
        else:
            print(f"You're supposed to say '{whosThere}'")
            
# if answer begins with "Y" start the knock knock joke, otherwise try to persuade them
else:
    if answer.startswith("Y"):
        print(knock)
        answer2 = input("")
        if answer2 == "Who's there?":
            print(art)
            answer3 = input("")
            if answer3 == "Art who?":
                print(r2d2)
            else:
                if answer3 == "art who?":
                    print(r2d2)
                else:
                    print(f"You're supposed to say '{artWho}'")
        else:
            if answer2 == "who's there?":
                print(art)
                answer3 = input("")
                if answer3 == "Art who?":
                    print(r2d2)
                else:
                    if answer3 == "art who?":
                        print(r2d2)
                    else:
                        print(f"You're supposed to say '{artWho}'")
            else:
                print(f"You're supposed to say '{whosThere}'")
    else:
        print("C'mon, you're really missing out!")
