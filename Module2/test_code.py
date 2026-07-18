# Secret Number Guessing Game

secret = 27
attempts = 5

print("🎮 Welcome to the Secret Number Game!")
print("Guess the secret number between 1 and 50.")
print("You have 5 attempts.\n")

while attempts > 0:

    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("🎉 Congratulations! You guessed the secret number.")
        break

    else:
        difference = abs(secret - guess)

        if difference > 20:
            print("🧊 Ice Cold!")
        elif difference > 10:
            print("🥶 Cold!")
        elif difference > 5:
            print("🌡️ Warm!")
        else:
            print("🔥 Hot!")

        attempts = attempts - 1

        if attempts > 0:
            print("Remaining Lives: ", end="")
            for i in range(attempts):
                print("❤️", end="")
            print("\n")

if attempts == 0:
    print("💀 Game Over!")
    print("The secret number was:", secret)