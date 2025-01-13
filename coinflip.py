import random

def coinflip():
    coin_sides = ["heads", "tails"]
    flipped = random.choice(coin_sides)
    
    print("Which side do you choose?: Heads or Tails?")
    userinput = input().lower()

    while userinput not in coin_sides:
        print("Invalid input")
        print("Which side do you choose?: Heads or tails?")
        userinput = input().lower()
    
    print(f"You chose: {userinput}!")
    print(f"The coin flips and lands on: {flipped}!")
    if userinput == flipped:
        print("You win!")
    else:
        print("You lose, better luck next time!")
        
    print("Play again? (Yes/No)")

    while True:
        again = input()
        if again == "yes".lower():
            coinflip()
        elif again == "no".lower():
            print("Goodbye")
            break
        else:
            print("Invalid input")

coinflip()