# Austin Avery
# Magic 8-Ball
# Friday May 17, 2024



import random

fortunes = [
    "Yes, definitely.",
    "It is certain.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Signs point to yes."
]

menuOptions = [
    "See all possible responses",
    "Choose a response by number",
    "Ask a question"
]

while True:
    print("Magic 8-ball Menu:")
    for i in range(len(menuOptions)):
        print(f"{i + 1}. {menuOptions[i]}")

    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        print("All possible responses:")
        for i in range(len(fortunes)):
            print(f"{i + 1}: {fortunes[i]}")
    elif choice == 2:
        try:
            num = int(input(f"Enter a number between 1 and {len(fortunes)}: "))
            if 1 <= num <= len(fortunes):
                print(f"You chose: {fortunes[num - 1]}")
            else:
                print("Invalid number. Please enter a number within the valid range.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == 3:
        question = input("Ask your question: ")
        print("Thinking...")
        response = random.choice(fortunes)
        print(f"The Magic 8-ball says: {response}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

    another = input("Do you want to ask another question? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print("Thank you for using the Magic 8-ball!")
