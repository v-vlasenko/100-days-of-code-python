# Go to README.md to check out exercise description
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

decision_images = [rock, paper, scissors]

player_decision = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: \n"))

if player_decision < 0 or player_decision > 2:
  print("You typed invalid number. Try again.")
else:
  print(decision_images[player_decision])
  
  computer_decision = random.randint(0, 2)
  computer_decision_image = decision_images[computer_decision]
  print("Computer chose: \n")
  print(computer_decision_image)
  
  if player_decision == 0 and computer_decision == 2:
    print("You win!")
  elif computer_decision == 0 and player_decision == 2:
    print("You lose!")
  elif player_decision > computer_decision:
    print("You win!")
  elif computer_decision > player_decision:
    print("You lose!")
  elif computer_decision == player_decision:
    print("It's a draw.")




  