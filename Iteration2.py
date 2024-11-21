import random 



print("Let's play rock, paper, scissors")

def get_user_choice():
  choice = input("Choose rock, paper, or scissors: ")
  return choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  cpu_choice = random.choice(choices)
  return cpu_choice



user_choice = get_user_choice()
computer_choice = get_computer_choice()
print(user_choice, computer_choice)
