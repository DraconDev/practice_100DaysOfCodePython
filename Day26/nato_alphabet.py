import pandas

test = ''

nato_alphabet = pandas.read_csv('./nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for i, row in nato_alphabet.iterrows()}


def spell_name():
    while True:
        name = input('Add a name\n')
        if all(letter.isalpha() for letter in name):
            try:
                return [nato_alphabet[letter] for letter in name.upper()]
            except KeyError:
                print('Invalid name')
        else:
            print('Name must contain only alphabets')


test = spell_name()

print(test)
