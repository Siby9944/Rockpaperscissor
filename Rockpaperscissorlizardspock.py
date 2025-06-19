#libraries
import random
from enum import IntEnum

class Action(IntEnum):
    Rock=0
    Paper=1
    Scissors=2
    Lizard=3
    Spock=4

victories={Action.Rock:[Action.Scissors,Action.Lizard],  # Rock beats Scissors, Lizard
               Action.Scissors:[Action.Paper,Action.Lizard],  # Scissors beats Paper, Lizard
               Action.Paper:[Action.Rock,Action.Spock] , 
                Action.Lizard:[Action.Paper,Action.Spock],
                Action.Spock:[Action.Scissors,Action.Rock]}

def user_Selection():
    user_input=input("Enter Rock[0],Paper[1],Scissors[2],Lizard[3],Spock[4]: ")
    selection=int(user_input)
    action=Action(selection)
    return action

def computer_Selection():
    computer_input=random.randint(0,len(Action)-1)
    action=Action(computer_input)
    return action

def winner(user_Action,computer_Action):
    defeats=victories[user_Action]

    if user_Action==computer_Action:
        print(f"Both players selected {user_Action.name}. It's a tie!")

    elif computer_Action in defeats:
        print(f"{user_Action.name} beats {computer_Action.name}! You win!")

    else:
        print(f"{computer_Action.name} beats {user_Action.name}! You lose!")

    
while True:
    try:
        user_Action=user_Selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_Action=computer_Selection()
    winner(user_Action,computer_Action)
    # Play again?
    play_again=input("Play again(Y/N):  ")
    if play_again.lower()=='n' or play_again.lower()=='no':
        break