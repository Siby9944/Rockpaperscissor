#Using IntEnum

#importing libraries
import random
from enum import IntEnum

#Defining action class
class Action(IntEnum):
    Rock=0
    Paper=1
    Scissor=2

#Define user input:
def user_selection():
    user_input=input("Enter one from following, Rock[0], Paper[1], Scissor[2]: ")
    selection=int(user_input)
    action=Action(selection)
    return action

#Define computer's random input:
def computer_selection():
    selection=random.randint(0,len(Action)-1)
    action=Action(selection)
    return action

#Determine the winner:
def determine_winner(user_action, computer_action):
    if user_action==computer_action :
        print(f"Both players selected {user_action}, It's a Tie")

    elif user_action == Action.Rock:
        if computer_action == Action.Scissor:
            print("Rock smashes scissors, You win")
        else:
            print("Paper covers Rock, You lose")

    elif user_action==Action.Scissor:
        if computer_action==Action.Paper:
            print("Scissors cuts Paper, You win")
        else:
            print("Rock smashes Scissors, You lose")

    elif user_action==Action.Paper:
        if computer_action==Action.Rock:
            print("Paper covers rock, You win")
        else:
            print("Scissors cuts Paper, You lose")

while True:
    try:
        user_action=user_selection()
    except ValueError as e:
        range_str=f"[0, {len(Action)-1}]"
        print("Invalid selection. Enter a value in range {}")
        continue

    computer_action=computer_selection()
    determine_winner(user_action,computer_action)

    # Play again?
    play_again=input("Play again(Y/N):  ")
    if play_again.lower()=='n' or play_again.lower()=='no':
        break