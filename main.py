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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.)"))
try:
  print(hand[user_choice])

  print("Computer chose:")
  computer_choice = random.randint(0,2)
  print(hand[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win")
  elif computer_choice == user_choice:
    print("It's a draw")
  
except IndexError:
  #if user_choice >= 3 or user_choice < 0:
  print("You've typed an invalid number, you lose.")


# if user_choice == rock:
#   if computer_choice == scissors:
#     print("You win")
#   elif computer_choice == paper:
#     print("You lose")
#   else:
#     print("Draw")

# elif user_choice == paper:
#   if computer_choice == rock:
#     print("You win")
#   elif computer_choice == scissors:
#     print("You lose")
#   else:
#     print("Draw")
# else:
#   if computer_choice == paper:
#     print("You win")
#   elif computer_choice == rock:
#     print("You lose")
#   else:
#     print("Draw")

