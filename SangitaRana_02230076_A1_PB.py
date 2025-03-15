
import random

# Function for the Guess Number Game
def guess_number_game():
    print("\nWelcome to the Guess Number Game!")
    lower = int(input("Enter the lower bound of the range: "))
    upper = int(input("Enter the upper bound of the range: "))
    secret_number = random.randint(lower, upper)
    attempts = 0

    while True:
        guess = int(input(f"Guess a number between {lower} and {upper}: "))
        attempts += 1
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
print("\n1. Guess Number Game")
guess_number_game()

# Function for the Rock-Paper-Scissors Game
def rock_paper_scissors_game():
    print("\nWelcome to Rock-Paper-Scissors!")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        break
print("\n2. Rock-Paper-Scissors Game")
rock_paper_scissors_game()

# Main program for Part B
def main():
    while True:
        print("\nGames Menu:")
        print("1. Guess Number Game")
        print("2. Rock-Paper-Scissors Game")
        print("3. Exit")
        choice = input("Select a game (1-3): ")

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors_game()
        elif choice == '3':
            print("Exiting the games. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 3.")

# Run the program
if __name__ == "__main__":
    main()