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
image = [rock, paper, scissors]
user = int(input("Please enter your choice: 0 for Rock, 1 for Paper, or 2 for Scissors?\n"))

if user >= 3 or user < 0:
    print("Invalid entry, you lose")
    exit()
else:
    print(image[user])

computer = random.randint(0, 2)
print(f"The Computer has chosen:")
print(image[computer])

if user == 0 and computer == 2:
    print("Congratulations you have won")
elif user == 2 and computer == 0:
    print("You Lose")
elif user > computer:
    print("Congratulations you have won")
elif computer == user:
    print("You have tied")
elif computer > user:
    print("You Lose")
