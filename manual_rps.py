# %%
import random

def get_computer_choice():
  options=["rock", "paper", "scissors"]
  random_selection = random.choice(options)
  return random_selection

def get_user_choice():
  guess = input("Please enter rock, paper or scissors")
  return guess

def get_winner(computer_choice, user_choice):
  winner=""
  if computer_choice=="rock" and user_choice=="scissors":
    winner="You lost"
  elif computer_choice=="rock" and user_choice=="paper":
    winner="You won!"
  elif computer_choice=="sciccors" and user_choice=="rock":
    winner="You won!"
  elif computer_choice=="sciccors" and user_choice=="paper":
    winner="You lost"
  elif computer_choice=="paper" and user_choice=="rock":
    winner="You lost"
  elif computer_choice=="paper" and user_choice=="scissors":
    winner="You won!"
  elif computer_choice==user_choice:
    winner="It is a tie!"
  return winner
  
def play():
  computer_choice=get_computer_choice()
  user_choice=get_user_choice()
  print(get_winner(computer_choice, user_choice))
  print(computer_choice)
  print(user_choice)

play()


# %%
