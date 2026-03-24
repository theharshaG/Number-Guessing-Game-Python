import random

number = random.randint(1, 10)
attempts = 0

while True:
    try:
        guess = int(input("Enter guess number (1-10): "))
    except ValueError:
        print("Enter numbers only")
        continue

    attempts += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct! You guessed in {attempts} attempts 🎉")
        break
