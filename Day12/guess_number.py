import random

difficulty_object = {'easy': 5, "hard": 10}
winning_number = random.choice([number for number in range(1, 101)])

print(winning_number)


def game():
    # tries = int(input("Add number of tries\n"))
    tries = difficulty()
    print(guess(tries))


def guess(tries):
    while tries > 0:
        guessed_number = int(input("Guess a number\n"))
        if guessed_number > winning_number:
            print("Too high", tries)
        elif guessed_number < winning_number:
            print("Too low", tries)
        elif guessed_number == winning_number:
            return ("You won")
        tries -= 1
    return ("You lost")


# def guess(tries):
#     guessed_number = int(input("Guess a number\n"))
#     if tries == 1:
#         return ("You lost")
#     elif guessed_number > winning_number:
#         print("Too high", tries)
#     elif guessed_number < winning_number:
#         print("Too low", tries)
#     elif guessed_number == winning_number:
#         return ("You won")
#     tries -= 1
#     guess(tries)


def difficulty():
    difficulty = input("easy or hard?\n")
    difficulty_object[difficulty]

    return difficulty_object[difficulty]


game()
