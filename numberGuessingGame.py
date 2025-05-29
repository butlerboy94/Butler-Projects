import random

def number_guessing_game():
    

    number = random.randint(1, 10) # Generate a number between 1, 10
    tries = 3
    print("Guess a number between 1 and 10!") # Introduction to start the game
    while tries > 0:
        print(f"You have {tries} guesses left.") # Let the player know how many tries they have left
        try:
            guess = int(input("Enter your guess: ")) # Ask the player for their guess
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

            # Validate the guess in the range and let player know how close
            
        if guess == number:
            print("Correct!")
            continue
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

        tries -= 1

    # let player know they are out of guesses

    print("You are out of guesses. The number was", number)
# Start the game when the script is ran
if __name__ == "__main__":
    number_guessing_game()