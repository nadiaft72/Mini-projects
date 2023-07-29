# Function to find the occurrences of a letter in the word.


def findLetter (x , strWord):
    # Create an empty list to store the positions where the letter is found.
    listOfPlaces = []
    a=0

    # Check if the letter is not found in the word.
    if strWord.find(x)== -1 :
        return -1
    else:
        # Find all occurrences of the letter in the word.
        start = strWord.find(x ,a)
        while start != -1 and start < len(strWord):
            # Store the position of the letter in the list.
            listOfPlaces.append(start)
            a = start +1
            start = strWord.find(x ,a)

        # Return the list of positions where the letter occurs in the word.
        return listOfPlaces



    return

#guess the word :)

# Word to guess.
strWord = "alphabet"

# List to display the guessed and hidden letters of the word.
listStr = [" _ "," _ "," _ "," _ "," _ "," _ "," _ "," _ "]

# Number of guesses allowed.
count = 10

# Counter for correctly guessed letters.
countOfCorrect = 0
print("you have 10 guess !") 

# Start the game loop until the player runs out of guesses or guesses the word correctly.
while count != 0 and countOfCorrect != len(strWord):
    
    x = input("enter a letter : ")

    # Find the positions of the guessed letter in the word.
    res = findLetter(x,strWord)
    
    # If the letter is found in the word.
    if res != -1 :
        if listStr[res[0]] == " _ " :
            
            # Update the list to reveal the correct letters at their respective positions.
            countOfCorrect += len(res)
            for i in range(0,len(res)):
                listStr[res[i]] = x
            
            # Print the updated word.
            print("".join(listStr))
    else :
        # If the letter is not found in the word, decrement the count of remaining guesses.
        count -= 1
        print("nope! you have ",count," guesses! :)")
        
# Display the final result based on the outcome of the game.
if count == 0 :
    print("maybe later!")
else: 
    print("yayyyyy ! :)")
