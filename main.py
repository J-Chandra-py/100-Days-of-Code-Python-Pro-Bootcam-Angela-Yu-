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

#Write your code below this line 👇

hand = [rock, paper, scissors]

user_value = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.)"))
user_choice = hand[user_value]
print(user_choice)

print("Computer chose:")
computer_choice = random.choice(hand)
print(computer_choice)

if user_choice == rock:
  if computer_choice == scissors:
    print("You win")
  elif computer_choice == paper:
    print("You lose")
  else:
    print("Draw")

elif user_choice == paper:
  if computer_choice == rock:
    print("You win")
  elif computer_choice == scissors:
    print("You lose")
  else:
    print("Draw")
else:
  if computer_choice == paper:
    print("You win")
  elif computer_choice == rock:
    print("You lose")
  else:
    print("Draw")