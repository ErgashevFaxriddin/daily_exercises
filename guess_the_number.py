import random

number = random.randint(1, 10)

guess = int(input("Guess number between 1 and 10: "))

if guess == number:
    print("Correct!")
else:
    print("Wrong, the number was", number)