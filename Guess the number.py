import random as rand

num = rand.randint(1, 100)

guess = int(input("Guess the number between 1 and 100: "))

while guess != num:
    if guess > 100 or guess < 1:
        print("Incorrect input")
        guess = int(input("Guess the number between 1 and 100: "))
    elif guess > num:
        print("Lower!")
        guess = int(input("Guess the number between 1 and 100: "))
    elif guess < num:
        print("Higher!")
        guess = int(input("Guess the number between 1 and 100: "))

print("You guessed it!")
