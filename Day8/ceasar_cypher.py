
import string

alphabet = list(string.ascii_lowercase)

instruction = input('encode or decode?\n').lower()
message = input('message\n').lower()
shift = int(input('shift by how many letters\n').lower())


def cypher(instruction, message, shift):

    solution = []
    if instruction == "encode":
        for letter in message:
            # solution.append(chr(ord(letter) + shift))
            if letter.isalpha():
                solution.append(chr((ord(letter) - 97 + shift) % 26 + 97))
            else:
                solution.append(letter)
    if instruction == "decode":
        for letter in message:
            if letter.isalpha():
                solution.append(chr((ord(letter) - 97 - shift) % 26 + 97))
            else:
                solution.append(letter)
    print("".join(solution))


cypher(instruction, message, shift)
