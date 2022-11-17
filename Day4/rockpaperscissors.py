import random

player_input = input("rock, paper or scissors?")


def rps(player_input):
    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    print(computer_choice)

    if player_input == computer_choice:
        print("tie")
    elif (player_input == "paper" and computer_choice == "rock") or (player_input == "rock" and computer_choice == "scissors") or (player_input == "scissors" and computer_choice == "paper"):
        print("You won")
    else:
        print("You lost")


rps(player_input)
