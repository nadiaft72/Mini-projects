# Import the random module to generate random numbers.
import random

# Ask the user if they want to roll a dice or not.
end = input("to roll a dice enter y if not enter n: ")

# Start a loop to keep rolling the dice as long as the user enters 'y'.
while end == "y":
    # Generate a random number between 1 and 6 to simulate a dice roll.
    x = random.randint(1,6)
    
    # Print the result of the dice roll to the user.
    print("your dice number is : ",x," \n")
    
    # Ask the user again if they want to roll the dice or not.
    end = input("to roll a dice enter y if not enter n: ")

# The loop ends when the user enters 'n'. Print a fun message to conclude the program.
print("\n have fun!")
