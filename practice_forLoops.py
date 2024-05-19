inventory = ["bone saw", "doily", "rubber chicken"]
monsters = ("bunny", "dragon", "crippling self-doubt")
numMonsters = len(monsters)

for item in inventory:
    print(f"You hit the dragon with {item}.")
print()

for monster in monsters:
    print(f"You attack the {monster} with the doily.")
print()

for i in range(5):
    print(i)
print()

for i in range(2, 6):
    print(i)
print()

for i in range(5, 25, 5):
    print(i)
print()

for i in range(5, 0, -1):
    print(i)
print()

for monsterNum in range(numMonsters):
    print(f"{monsterNum}: {monsters[monsterNum]}")
print()

for (id, monster) in enumerate(monsters):
    print(f"{id}: {monster}")
print()

    
    