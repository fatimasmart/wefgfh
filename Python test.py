import random
secret = random.randint(1, 50)
attempts = 5
won = False

print("Welcome to the Number Guessing Game!")

while attempts > 0 and not won:
    guess = int(input("Enter a number (1-50): "))
    if guess == secret:
        print("You won!")
        won = True
    else:
        attempts = attempts - 1
        diff = abs(guess - secret)
        if diff >= 20:
            print("Hint: Ice cold 🧊")
        elif diff >= 10:
            print("Hint: Cold 🥶")
        elif diff >= 5:
            print("Hint: Warm 🌡️")
        else:
            print("Hint: Hot 🔥")
        print("Remaining lives: ", end="")
        for i in range(attempts):
            print("❤️", end="")
        print("\n")

if not won:
    print("Game over! The secret number was:", secret)