# Number Guessing Game:
# Generate a random number and prompt the user to guess it. Give hints such as "higher" or "lower" until they guess the correct number.
import random

randomNumber = random.randint(1,100)

# keep promting the user for input until the number is guessed correcly

# while True:
#    guessPrompt = int(input("I'm thinking of a number..." "\nGuess a number between 1-100: "))
#    if guessPrompt > randomNumber:
#        print("Guess lower")
#    elif guessPrompt < randomNumber:
#        print("Guess higher")
#    elif guessPrompt == randomNumber:
#        print("Congrats!", guessPrompt, "was the number")
#        break

# with error handling

print("I'm thinking of a number...")

while True:
    try:
        guessPrompt = int(input("Guess a number between 1-100: "))
    except ValueError:
        # incase the user enter nothing
        print("Please enter a valid number")
        continue
    if 1 <= guessPrompt <= 100:
            if guessPrompt > randomNumber:
                print("Guess lower")
            elif guessPrompt < randomNumber:
                print("Guess higher")
            elif guessPrompt == randomNumber:
                print("Congrats!", guessPrompt, "was the number")
                break
    else:
         print("Please enter a number between 1 and 100.")
