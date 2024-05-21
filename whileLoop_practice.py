
tripFinished = "NO"
while tripFinished != "YES":
    print("We're still driving...")
    
    tripFinished = input("Are we there yet? ")
    tripFinished = tripFinished.upper()

print("Can we go home now?")

print("Pick a number between 50-59")
number = input("")
number = int(number)
while number < int("55") or number > int("55"):
    print("Thats not the right number")
    
    number = input("Choose a new number: ")
    number = int(number)
    
print("Good job")


keepGoing = True
while keepGoing:
    print("We're still driving...")
    
    tripFinished = input("Are we there yet? ")
    tripFinished = tripFinished.upper()
    if tripFinished.startswith("Y"):
        keepGoing = False

print("Can we go home now?")
