print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.".` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

hand = input("You find a sword on the ground but forget which arm is dominant. \n"
             "pick it up with your left or right hand? Type 'left' or 'right': ")

if hand == 'right':
    print("You pick it up and put it in your right hand. A dragon attacks! You try to swing\n"
          "but your arm flails awkwardly in front of you and you are eaten by the dragon.")
    print("Game over!")
    quit()
elif hand == 'left':
    print("You pick up the sword and put it in your left hand. A dragon attacks! You swing furiously\n"
          "and strike the dragon in the neck!")
    water = input("You've come to a river. You can wait for the ferry or try to swim across.\n"
                  "Type 'swim' or 'wait': ")
    if water == "swim":
        print("You get in the water but halfway through realize it's an acid lake! You try to swim back\n"
              "but just as you realize the boat is made of polytetrafluoroethylene, you dissolve before\n"
              "reaching the bottom.")
    elif water == "wait":
        print("You wait for the boat because you dont want to get in. The ferry captain informs \n"
              "you the lake is actually acid. Your laziness saves you and you live to lie on the\n"
              " couch another day.")
        door = input("You come to stairs going deep into the earth. At the bottom there are three doors, each\n"
                     "with their own color. Type 'red', 'blue', or 'yellow' to enter the corresponding door: ")
        if door == "red":
            print("You open the red door, RUSH in and....fall into a pit of spikes, you die a gruesome death.\n"
                  "Better luck next time!")
            quit()
        elif door == "blue":
            print("You open the blue door and out walks an ogre! The ogre takes your sword and plunges it into\n"
                  "your left foot! He shuts the door shouting 'KNOCK FIRST' and locks it. The ground is solid\n"
                  "and you're unable to pull the sword out or move. You die of starvation.")
            quit()
        elif door == "yellow":
            print("You pick the color of gold...ish...well it's yellow but you're too dumb to know the difference.\n"
                  "You enter a cavern leading to a room with a portal. You go through the portal and are transported\n"
                  "to a mansion full of gold, members of the same and / or opposite sex that find you attractive\n"
                  "and share your common interests (if you're into that sort of thing), and 63 buckets of \n"
                  "KFC fried chicken. Life is good.")
            quit()
    else:
        print("You didn't pick a valid choice. You are eaten by a dragon.")
else:
    print("You didn't pick a valid choice. You are eaten by a dragon.")
