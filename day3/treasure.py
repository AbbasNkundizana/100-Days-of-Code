
print("Welcome to the treasure hunt.\nYour mission is to find the treasure")
choice1 = input('Please chose a route to take "left" or "right": ').lower()
if (choice1 == "left"):
    #proceed
    choice2 = input('Please proceed to select a convayence means "boat" or "canoe": ').lower()
    if (choice2 == "canoe"):
        #proceed
        choice3 = input('Please proceed to select a door of your choice "orange", "red", or "green": ').lower()
        if (choice3 == "green"):
            print(''' Hooraaaay! you have found the treasure
******************************************
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
        else:
            print("Sorry mate, you have hit a dead end! Game over")
    else:
          print("Sorry mate the boat engine is broken and wont move! Game over.")
else:
    print("Sorry mate you have hit a wall! Game over.")













