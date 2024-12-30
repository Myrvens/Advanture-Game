name = input("Type your name: ")
print(f"Welcome, {name}, to this magical adventure!")

print("Your journey begins on a quiet dirt road surrounded by a dense forest.")
answer = input(
    "You come to a fork in the road. Would you like to go left, right, or straight? ").lower()

if answer == "left":
    answer = input(
        "You walk down a path and come across a wide river. It's fast-flowing and looks dangerous. "
        "Do you swim across, build a raft, or turn back? (swim/raft/back): ").lower()

    if answer == "swim":
        print("You bravely dive into the river, but unfortunately, you are swept away by the current. Game over.")
    elif answer == "raft":
        print(
            "You spend some time building a raft and safely cross the river. On the other side, you find a hidden treasure chest full of gold! You WIN!")
    elif answer == "back":
        print("You head back to the start, feeling defeated. Game over.")
    else:
        print("Not a valid option. You stand there confused until night falls. Game over.")

elif answer == "right":
    answer = input(
        "You come to a wobbly bridge over a deep canyon. Do you cross it, inspect it, or go back? (cross/inspect/back): ").lower()

    if answer == "cross":
        print(
            "You carefully cross the bridge, but halfway through, it collapses, and you fall into the canyon. Game over.")
    elif answer == "inspect":
        print(
            "You notice a secret lever near the bridge. Pulling it reveals a hidden, sturdy bridge nearby. You safely cross and find a map leading to an ancient castle. You WIN!")
    elif answer == "back":
        print("You decide to go back to the fork and start over. Game over.")
    else:
        print("Not a valid option. You lose your footing and fall into the canyon. Game over.")

elif answer == "straight":
    answer = input(
        "You venture straight into the forest. It's dark and eerie. After some time, you see a glowing light in the distance. "
        "Do you follow the light, explore deeper into the forest, or set up camp? (light/explore/camp): ").lower()

    if answer == "light":
        answer = input(
            "You follow the light and find a mystical fairy who offers you a wish. Do you wish for wealth, adventure, or knowledge? (wealth/adventure/knowledge): ").lower()

        if answer == "wealth":
            print("The fairy grants you unimaginable riches. You WIN!")
        elif answer == "adventure":
            print(
                "The fairy transports you to a dragon's lair, where your journey continues. The adventure never ends! You WIN!")
        elif answer == "knowledge":
            print("The fairy grants you infinite wisdom. You WIN!")
        else:
            print("The fairy disappears, and you are left in the dark forest. Game over.")
    elif answer == "explore":
        print("You explore deeper into the forest but get hopelessly lost. Game over.")
    elif answer == "camp":
        print("You set up camp and rest for the night. In the morning, you find a hidden path leading to a magical city. You WIN!")
    else:
        print("Not a valid option. You wander aimlessly until you are lost. Game over.")

else:
    print("Not a valid option. You stand still until night falls, and mysterious creatures surround you. Game over.")

print(f"Thank you for playing, {name}! Try again for a different adventure!")
