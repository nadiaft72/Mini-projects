# Import the random module to generate a random number.
import random

# Generate a random number between 1 and 100 (inclusive) and store it in 'x'.
x = random.randint(1, 100)

# For debugging purposes, print the randomly generated number.
print("Random number:", x)

# Ask the user to guess a number between 1 and 100 and convert the input to an integer.
Gnum = int(input("Guess a number (1-100): "))

# Start a loop to keep prompting the user for guesses until the correct number is guessed.
while Gnum != x:
    # If the guessed number is greater than the random number.
    if Gnum > x:
        print("Your guess is higher than mine! :)")
    # If the guessed number is less than the random number.
    elif Gnum < x:
        print("Your guess is lower than mine! :)")

    # Ask the user to guess again and update 'Gnum' with the new guess.
    Gnum = int(input("Guess a number (1-100): "))

# The loop ends when the user guesses the correct number.
print("Yay, you did it! :) ")
