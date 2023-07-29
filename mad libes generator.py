# Initialize 'end' to 'y' to start the loop for generating Mad Libs.
end = 'y'

# Start a loop to generate Mad Libs as long as the user wants to continue ('end' is 'y').
while end == 'y':

    # Ask the user to input various words to fill in the Mad Libs template.
    Occupation1 = input("Give me an Occupation (a job): ")
    Noun2 = input("Give me a Noun: ")
    Adjective3 = input("Give me an Adjective: ")
    Noun4 = input("Give me a Noun: ")
    Verb5 = input("Give me a Verb: ")
    Adjective6 = input("Give me an Adjective: ")
    Noun7 = input("Give me a Noun: ")
    Verb8 = input("Give me a Verb: ")
    Noun9 = input("Give me a Noun: ")
    Verb10 = input("Give me a Verb: ")

    # Generate the Mad Libs story using the user's inputs and print it.
    print("Today a", Occupation1, "named", Noun9, "came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to", Verb8, "around (a)", Adjective3, Noun7,
          ". She said it was easy for her to learn her job because she loved to", Verb5, "when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a)", Adjective6,
          Noun2, ". That's very important! If you get too distracted in that situation you won't be able to", Verb10, "next to (a)", Noun4, "!")

    # Ask the user if they want to generate another Mad Libs.
    end = input("Again? (y/n) ")

# The loop ends when the user enters 'n'. Print a fun message to conclude the program.
print("\nHave fun! :)")
