from day14art import vs
from day14gamedata import data
import random
from clear import clear


def generate_item(saved_item):
    new_item = random.choice(data)
    while new_item == saved_item:
        new_item = random.choice(data)
    return new_item


def play_game(item1_val, item2_val, score):
    print(f"Compare A: {item1_val['name']}, a {item1_val['description']}, from {item1_val['country']}.")
    print(vs)
    print(f"Against B: {item2_val['name']}, a {item2_val['description']}, from {item2_val['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if item1_val['follower_count'] > item2_val['follower_count']:
        winner = 'a'
    else:
        winner = 'b'
    if guess == winner:
        clear()
        score += 1
        print(f"You're right! Current score: {score}")
        next_item = generate_item(item2_val)
        play_game(item2_val, next_item, score)
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")


def start_game():
    item1 = random.choice(data)
    item2 = generate_item(item1)
    clear()
    play_game(item1, item2, 0)


start_game()
