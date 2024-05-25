def getGame():
    game = {
        "start": ["You and three buddies are injured while trekking a mountain range. Wolves notice and start their hunt.", "Stand your ground and fight the wolves", "stand", "Turn and try to run away", "run"], 
        "stand": ["Did I forget to mention you're already injured and being hunted BY WOLVES?", "Stay and try to fight the wolves off", "fight", "Turn and try to run away", "run"], 
        "run": ["You and your buddies manage to get some distance from the wolves. But you're near a cliff side.", "Stay and shelter in place", "stay", "Keep moving", "move"], 
        "fight": ["You and your buddies don't have the strength to fight. You managed to escape but the wolves got your buddies.", "Move on and look for shelter", "shelter", "Go back for your buddies", "buddies"], 
        "stay": ["You forage the area and find enough to build a small shelter. Do you:", "Split up to gather firewood and food", "split", "Get some rest", "rest"], 
        "move": ["You're all extremely exhausted. The wolves catch up and have a little snack.", "Start over", "start", "Quit", "quit"], 
        "shelter": ["You find a little cove in the mountainside and decide to rest there for the night. Unbeknownst to you the cove is a den for a Momma bear and her cubs.", "Start over", "start", "Quit", "quit"], 
        "buddies": ["You manage to get back to where the wolves took your buddies and see trails of blood going deeper into the mountain.", "Start over", "start", "Turn back and search for shelter", "shelter"], 
        "split": ["While you were split up you were vulnerable. The wolves split and we're able to take you all out.", "Start over", "start", "Quit", "quit"], 
        "rest": ["You're all feeling overwhelming lucky the wolves didn't attack at night. But also, starving.", "Split up to gather firewood and food", "split", "Start your trek back to civilization", "trek"], 
        "trek": ["On your way back you stumble upon a stream of water filled with fish.", "Fish for food", "fish", "Continue your hike back", "hike"], 
        "fish": ["While you were fishing a bear snuck up on your group and had a little snack.", "Start over", "start", "Quit", "quit"], 
        "hike": ["You and your buddies can finally see a little village. You all start running in joy and make it out alive!", "Start over", "start", "Quit", "quit"] 
    }
    return game

def playerNode(game, currentNode):
    keepGoing = True
    value = game[currentNode]
    description, menuA, nodeA, menuB, nodeB = value
    print(description)
    
    while(keepGoing):
        print(f"""
            1) {menuA}
            2) {menuB}""")
        playerChoice = input("Your choice: ").strip()
        if playerChoice == "1":
            return nodeA
        elif playerChoice == "2":
            return nodeB
        else:
            print("Please choose a number. Try again.")

def main():
    game = getGame()
    keepGoing = True
    currentNode = "start"

    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else:
            currentNode = playerNode(game, currentNode)

main()
