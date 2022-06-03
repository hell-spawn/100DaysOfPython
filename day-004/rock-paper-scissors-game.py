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
user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user = int(user)
map = [rock, paper, scissors]

machine = random.choice([0,1,2])
print("User choice:")
print(map[user])
print("Machine choice:")
print(map[machine])

if(user == 0):
    if(machine == 0):
        print("It's a draw")
    elif(machine == 1):
        print("You lose")
    else:
        print("You win!")
elif(user == 1):
    if(machine == 0):
        print("You win!")
    elif(machine == 1):
        print("It's a draw")
    else:
        print("You lose")
else:
    if(machine == 0):
        print("You lose")
    elif(machine == 1):
        print("You win!")
    else:
        print("It's a draw")
