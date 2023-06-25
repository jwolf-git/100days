import random


def compare(player_guess, true_number):
    if player_guess == true_number:
        print(f"You got it! The answer was {true_number}.")
        replay = input("Would you like to play again(enter 'y' or 'n')? ")
        if replay == 'y':
            play_game()
        else:
            quit()
    elif player_guess > true_number:
        print("Too high.\nGuess Again.")
    elif player_guess < true_number:
        print("Too low.\nGuess again.")


def play_game():
    print("Welcome to the number guessing game")
    difficulty = input("Choose a difficulty, 'easy' or 'hard': ").lower()
    tries = 0
    number = random.randint(1, 100)

    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'hard':
        tries = 5
    else:
        print("Invalid input, goodbye")
        quit()
    
    while tries != 0:
        guess = int(input("Make a guess: "))
        compare(guess, number)
        tries -= 1
        if tries == 0:
            print("You've run out of guesses, you lose.")
            quit()
        print(f"You have {tries} attempts remaining to guess the number.")


play_game()
