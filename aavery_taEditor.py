def main():
    game = getDefaultGame()
    keepGoing = True
    
    while keepGoing:
        userChoice = getMenuChoice()
        if userChoice == "0":
            print("\n    Exiting program...")
            keepGoing = False
        else:
            if userChoice == "1":
                print("\n    Default game loaded.")
                game = getDefaultGame()
            elif userChoice == "2":
                print("\n    Loading...")
                game = loadGame()
            elif userChoice == "3":
                print("\n    Saving...")
                saveGame(game)
            elif userChoice == "4":
                print("\n    Editor Mode...\n")
                editNode(game)
            elif userChoice == "5":
                print("\n    Playing game.\n")
                playGame(game)
            else:
                print("\nInvalid input. Please enter a number (0-5).")
    
def getMenuChoice():
    menu = ("""
    Menu options:
    0) exit
    1) load default game
    2) load a game file
    3) save the current game
    4) edit or add a node
    5) play the current game
    """)
    print(menu)
    userChoice = input("    Your choice: ").strip()
        
    return userChoice

def getDefaultGame():
    defaultGame = {
        "start": ["Default Game Node", "Start over", "start", "Go back to main menu", "quit"]
        }
    return defaultGame

def playGame(game):
    keepGoing = True
    currentNode = "start"

    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playNode(game, currentNode)

def playNode(game, currentNode):
    keepGoing = True
    value = game[currentNode]
    description, menuA, nodeA, menuB, nodeB = value
    print(description)
    
    while keepGoing:
        print(f"""
            1) {menuA}
            2) {menuB}
            """)
        userChoice = input("Your choice: ").strip()
        if userChoice == "1":
            currentNode = nodeA
        elif userChoice == "2":
            currentNode = nodeB
        else:
            print("\nPlease enter a number (1 or 2).\n")
        
        return currentNode

def saveGame(game):
    import json
#    savedGame = getDefaultGame()
    outFile = open("game.dat", "w")
    json.dump(game, outFile, indent=2)
    outFile.close()
    print(json.dumps(game, indent=2))
    print("\n    Saved game to game.dat")
    
def loadGame():
    import json
    inFile = open("game.dat", "r")
    loadedGame = json.load(inFile)
    inFile.close()
    print(json.dumps(loadedGame, indent=2))
    print("\n    Loaded game from game.dat")
    
    return loadedGame
    
def editField(newValue, oldValue):
    value = input(f"{newValue} ({oldValue}): ")
    if value == oldValue:
        newValue = oldValue
    return value

def editNode(game):
    import json
    
    print("    Current status of game:")
    print(json.dumps(game, indent=2))
    
    print("Existing node names:")
    for nodeNames in game:
        values = game[nodeNames]
        print(nodeNames)
        
    newNodeName = input("Name of node to edit or create? ")
    if newNodeName in game.keys():
        newNode = game[newNodeName]
    else:
        newNode = ("", "", "", "", "")
    
    description, menuA, nodeA, menuB, nodeB = newNode
#    for nodeNames in game:
    newDescription = editField("Description", description)
    newMenuA = editField("Menu A", menuA)
    newNodeA = editField("Node A", nodeA)
    newMenuB = editField("Menu B", menuB)
    newNodeB = editField("Node B", nodeB)
    
    newNode = newDescription, newMenuA, newNodeA, newMenuB, newNodeB
    game[newNodeName] = newNode
    
main()