import random


def guess_the_number(attempts):
    print(f"\nYou have {attempts} attempts to guess the number!")
    target_number = random.randint(1, 100)
    guess = None
    attempts_left = attempts

    while attempts_left > 0 and guess != target_number:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts_left -= 1

        if guess < target_number:
            print("Too low.")
        elif guess > target_number:
            print("Too high.")
        else:
            print(f"Congratulations! You've guessed the number {target_number}!")
            break

        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left.")
        else:
            print(f"Sorry, you've run out of attempts. The number was {target_number}.")


def select_difficulty():
    print("Select Difficulty Level:")
    print("1: Easy (10 attempts)")
    print("2: Hard (5 attempts)")
    while True:
        choice = input("Enter the difficulty level (1 or 2): ")
        if choice == "1":
            return 10
        elif choice == "2":
            return 5
        else:
            print("Invalid choice. Please select 1 for Easy or 2 for Hard.")


def play_again():
    while True:
        attempts = select_difficulty()
        guess_the_number(attempts)
        play_again = input("\nDo you want to play again? Type 'y' for yes or 'n' for no: ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break


# Start the game
play_again()
