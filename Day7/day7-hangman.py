# A simple hangman game
import random
import hangman_art
import hangman_words

# Variables
stages = hangman_art.stages
end_of_game = False
lives = len(stages)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
prev_guess = []

# Debugging
# print(f"Psst, the random word is {chosen_word}")

# Sets "display" list to empty
for _ in range(word_length):
    display += "_"

print(hangman_art.logo)
print("Welcome to hangman!")
# Game loop
while not end_of_game:
    change = False
    guess = input("Guess a letter: ").lower()

    # Compare with previous guesses
    for test_letter in prev_guess:
        if guess == test_letter:
            print("You've already guessed this letter ya big dummy")
    prev_guess.append(guess)
    prev_guess = [*set(prev_guess)]

    # Check guessed letter against the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        # Debugging
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            change = True

    print(f"{' '.join(display)}")

    if not change:
        print("Wrong!")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("You lose!")
            quit()

    # Join all the elements in the list and turn it into a String.

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
