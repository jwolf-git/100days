import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

player_selection = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors."))
if player_selection > 2:
    print("You lose! Invalid choice!")
    quit()

computer_selection = random.randint(0, 2)

game_icons = (rock, paper, scissors)
game_titles = ("rock", "paper", "scissors")
game_field = (game_icons, game_titles)

print("You chose " + game_titles[player_selection] + "!\n" + game_icons[player_selection])
print("The computer chose " + game_titles[computer_selection] + "!\n" + game_icons[computer_selection])

if player_selection == 0 and computer_selection == 2 or player_selection == 2 and computer_selection == 1\
        or player_selection == 1 and computer_selection == 0:
    print("You win!")
elif computer_selection == 0 and player_selection == 2 or computer_selection == 2 and player_selection == 1\
        or computer_selection == 1 and player_selection == 0:
    print("The computer wins!")
elif computer_selection == player_selection:
    print("Draw! Try again!")
else:
    print("Invalid choice! Try aggggggain!")
