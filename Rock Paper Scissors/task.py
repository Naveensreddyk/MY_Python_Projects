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
print("Welcome to the rock, paper and scissors Game Tournament")
choices = ["rock", "paper", "scissors"]
your_choice= int(input("Choose 0 for rock, choose 1 for paper and choose 2 for scissors\n"))
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
elif your_choice == 2:
    print(scissors)
else:
    print("Choose the correct number")

computer_choice= random.randint(0, 2)
print(computer_choice)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)
else:
    print("INVALID RESPONSE")

if your_choice == computer_choice:
    print("It's a Draw")
elif your_choice == 1 and computer_choice == 0:
    print("YOU WIN")
elif your_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif your_choice == 2 and computer_choice == 1:
    print("YOU WIN")
else:
    print("YOU LOSE")
