dir = input("hello! if you wanna to win you have to found the right way... \n so which one do you choose? left or right? (l/r) ")
if dir == "l":
    dir = input("you came to the bear room, so if you choose a bad way you loose! now go! (l/r) ")
    if(dir == "r"):
        print("you win :) ")
    elif dir == "l":
        print("oh no!!! :((")
    else : 
        print ("wrong awnser... you loose!")
if dir == "r":
    dir = input("you came to the monster room, so if you choose a bad way you loose! now go! (l/r) ")
    if(dir == "l"):
        print("you win :) ")
    elif dir == "r":
        print("oh no!!! :((")
    else : 
        print ("wrong awnser... you loose!")