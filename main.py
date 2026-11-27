import random

TESTING = True  # testing ke liye True, normal game ke liye False
MAX_ATTEMPTS = 5


def play_game():
    secret = 42 if TESTING else random.randint(1, 100)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        guess = input("Enter your guess (1-100): ")

        # validation: sirf whole number
        if not guess.isdigit():
            print("Invalid input. Enter a whole number.")
            continue

        guess = int(guess)

        # validation: range check
        if guess < 1 or guess > 100:
            print("Out of range. Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret:
            print(f"Congratulations! You guessed it in {attempts} attempt.")
            return
        elif guess < secret:
            print(f"Too low! Attempts left: {MAX_ATTEMPTS - attempts}")
        else:
            print(f"Too high! Attempts left: {MAX_ATTEMPTS - attempts}")

    print(f"Game Over! The number was {secret}.")


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()
