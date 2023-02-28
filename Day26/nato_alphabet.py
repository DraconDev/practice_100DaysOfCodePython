import pandas

test = ''

nato_alphabet = pandas.read_csv('./nato_phonetic_alphabet.csv')

# print(nato_alphabet.iterrows())

# nato_alphabet_dict = {}
# for (i, row) in nato_alphabet.iterrows():
#     nato_alphabet_dict[row.letter] = row.code
# nato_alphabet = nato_alphabet_dict

nato_alphabet = {row.letter: row.code for i, row in nato_alphabet.iterrows()}

# test = nato_alphabet

# with open('test.txt', 'w') as f:
#     f.write(str(test))


def spell_name():
    print('Add a name')
    name = input()

    # letters = list(name.upper())
    # letters = name.upper()[:]

    # return [nato_alphabet[letters[i]] for i in range(len(letters))]

    return [nato_alphabet[letter] for letter in name.upper()[:]]


test = spell_name()

print(test)
