import random
bag=['mango', 'apple', 'orange', 'banana']
print("Guess the game : apple, orange, banana, mango")
word=random.choice(bag)
while True:
    user=input("Enter a fruite name :")
    if user not in bag:
        print("Given name is not in the list")
    if user==word:
        print("you guessed right")
        play_again=input("Do u want to play again ? [y/n]:")
        if play_again=='y':
            user=input("Enter the fruit name:")
        else:
            break
    else:
        print("Please try again")
