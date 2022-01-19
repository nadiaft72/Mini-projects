import random

x = random.randint(1,100)
print(x)
Gnum = int(input("guess a number (1-100): "))
while Gnum != x :
    if Gnum > x :
        print("ur guess is higher than mine ! :)")
    elif Gnum < x :
        print("ur guess is lower than mine ! :)")
    Gnum = int(input("guess a number (1-100): "))


print ("yay you did it! :) ")
