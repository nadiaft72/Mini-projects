# Ask the user to choose a direction (left or right) to start the adventure.
dir = input("Hello! If you want to win, you have to find the right way...\nSo which one do you choose? Left or right? (l/r) ")

# Check the user's first choice (left).
if dir == "l":
    # Ask the user to choose a direction (left or right) in the bear room.
    dir = input("You came to the bear room. If you choose the wrong way, you lose! Now, go! (l/r) ")
    
    # Check the user's choice in the bear room.
    if dir == "r":
        print("You win! :)")  # The user chose the correct way in the bear room.
    elif dir == "l":
        print("Oh no!!! :((")  # The user chose the wrong way in the bear room.
    else:
        print("Wrong answer... You lose!")  # Invalid input in the bear room.

# Check the user's first choice (right).
if dir == "r":
    # Ask the user to choose a direction (left or right) in the monster room.
    dir = input("You came to the monster room. If you choose the wrong way, you lose! Now, go! (l/r) ")
    
    # Check the user's choice in the monster room.
    if dir == "l":
        print("You win! :)")  # The user chose the correct way in the monster room.
    elif dir == "r":
        print("Oh no!!! :((")  # The user chose the wrong way in the monster room.
    else:
        print("Wrong answer... You lose!")  # Invalid input in the monster room.
