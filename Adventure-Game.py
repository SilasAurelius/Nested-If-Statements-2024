# Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("Light a torch or proceed in the dark? ")
    if action == "Light a torch":
        print("You find a hidden treasure!")
    elif action == "proceed in the dark":
        print("You fumble around the dark until you find a hidden goblin village.\n They welcome you and you even settle down and start a family. \n You live happily ever after!")
    else:
        pass
else:
    pass
    
# Task 2: Setting the Scene: Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.  