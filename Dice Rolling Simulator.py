import random
end = input("to roll a dice enter y if not enter n: ")
while end == "y":
    x = random.randint(1,6)
    print("your dice number is : ",x," \n")
    end = input("to roll a dice enter y if not enter n: ")
print("\n have fun!")