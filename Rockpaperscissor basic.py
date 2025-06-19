#Scissors->Paper->Rock->Scissors
#Basic method using Strings
#importing libraries
import random

while True:
    #Define user input:

    user_input=input("Enter one from following, Rock, Paper, Scissors: ")

    #Define computer's random input:

    list=['Rock','Paper','Scissors']
    computer_input=random.choice(list)

    print(f"You choose {user_input}, computer choose {computer_input}")

    #Determine the winner:

    if user_input==computer_input :
        print(f"Both players selected {user_input}, It's a Tie")

    elif user_input=='Rock':
        if computer_input=='Scissors':
            print("Rock smashes scissors, You win")
        else:
            print("Paper covers Rock, You lose")

    elif user_input=='Scissors':
        if computer_input=='Paper':
            print("Scissors cuts Paper, You win")
        else:
            print("Rock smashes Scissors, You lose")

    elif user_input=='Paper':
        if computer_input=='Rock':
            print("Paper covers rock, You win")
        else:
            print("Scissors cuts Paper, You lose")

    # Play again?
    play_again=input("Play again(Y/N):  ")
    if play_again.lower()=='n' or play_again.lower()=='no':
        break


