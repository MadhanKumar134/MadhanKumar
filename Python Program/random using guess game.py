import random
bag=['mango','apple','banana','orange']
print("Guess the fruit name: apple,banana,mango,orange")
word=random.choice(bag)
while True:
    user=input("Enter the Fruit name: ")
    if user==word:
        print("you guessed right")
        break
    else:
        print("please try again")








    
