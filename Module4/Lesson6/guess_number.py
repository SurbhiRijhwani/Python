import random
import time


def intro():
    print("May I ask you for your name?")

    global name
    name = input()

    print(
        name
        + ", we are going to play a game. I am thinking of a number between 1 and 100."
    )

    if number % 2 == 0:
        x = "even"
    else:
        x = "odd"

    print("\nThis is an {} number.".format(x))

    time.sleep(0.5)
    print("Go ahead. Guess!")


def pick():
    guessesTaken = 0

    # The number of guesses is limited to 6
    while guessesTaken < 6:
        time.sleep(0.25)

        enter = input("Guess: ")

        try:
            # Convert the input into an integer
            guess = int(enter)

            # Check if the guess is in range
            if guess >= 1 and guess <= 100:
                guessesTaken += 1

                if guess < number:
                    print("The number you entered is too low.")

                elif guess > number:
                    print("The number you entered is too high.")

                else:
                    # Correct guess
                    break

                if guessesTaken < 6:
                    time.sleep(0.5)
                    print("Try Again!")

            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100.")

        except ValueError:
            print("I don't think that " + enter + " is a number. Sorry!")

    # Check whether the player guessed correctly
    if guess == number:
        print(
            "Good job, {}! You guessed my number in {} guesses!".format(
                name, guessesTaken
            )
        )
    else:
        print("Nope. The number I was thinking of was " + str(number))


# Main game loop
playagain = "yes"

while playagain.lower() in ["yes", "y"]:

    # Generate a new number for every new game
    number = random.randint(1, 100)

    intro()
    pick()

    print("Do you want to play again?")
    playagain = input()