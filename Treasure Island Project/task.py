from tkinter.constants import RIGHT

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
level_1 = input(" You are on LEVEL 1. Choose Left or Right\n").lower()
if level_1 == "left":
   level_2= input("You have reached level 2 and there is magical ocean with mythical creatures. You have two options Wait or Swim\n").lower()
   if level_2 == "wait":
       level_3 = input("Thank you for the wait. You have reached level 3 and there are three islands. Choose 1, 2 or 3\n").lower()
       if level_3 == "1":
           print("You have chosen the island of snakes. GAME OVER")
       elif level_3 == "2":
             level_4 = input("You have chosen the treasure island. You have three doors in front of you Red, Yellow and Blue\n").lower()
             if level_4 == "red":
                 print("You have chosen the room full of fire. GAME OVER")
             elif level_4 == "yellow":
                 print("You have chosen the room full of sand. GAME OVER")
             elif level_4 == "blue":
                 print("CONGRATULATIONS, You have found the treasure.")
       elif level_3 == "3":
           print("You have chosen the island of Dragons. GAME OVER")
   else:
       print("You are eaten by Mythical Creatures. GAME OVER")


else:
    print("You have chosen the wrong direction and stepped into the forest. GAME OVER.")




