import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Keep track of the number of guesses
num_guesses = 0

# Loop until the user guesses the number
while True:
    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))
    num_guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", num_guesses, "guesses!")
        break
    elif guess < number:
        print("Your guess is too low, try again.")
    else:
        print("Your guess is too high, try again.")
