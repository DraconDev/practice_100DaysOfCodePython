solution = list(input("Solution word"))
guess = ["_" for i in solution]
tries = 8


def guessing(tries):
    while tries:
        guessed_letter = input("guess a letter\n")
        if guessed_letter in solution:
            print("hit")
            for i in range(len(solution)):
                if guessed_letter == solution[i]:
                    guess[i] = solution[i]
        else:
            tries -= 1
        print(guess)
        # print('test', solution)
        if solution == guess:
            tries = 0
            print("you won")
        elif tries == 0:
            print("You lost")
        else:
            print(f"remaining tries:{tries}")


guessing(tries)
