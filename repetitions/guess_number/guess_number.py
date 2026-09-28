import random

attempts = 0

guess = random.randint(1,100)

while True:
    num = int(input("Guess a number between 1 and 100: "))
    if num < guess:
        attempts += 1
        print("Too low")
    elif num > guess:
        attempts += 1
        print("Too high")
    elif num == guess:
        print(f"Correct! You guessed it in {attempts} attempts")
        break
