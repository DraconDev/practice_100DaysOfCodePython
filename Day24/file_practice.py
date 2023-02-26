# import os

# print(os.path.abspath('.'), 'test')

# with open("test.txt", 'a') as file:
#     # file.read()
#     file.write('sexy')
#     # print(file)

# with open("test.txt") as file:
#     text = file.read()
#     # print(text)

# with open("test2.txt", 'a') as file:
#     # print(file)
#     # file.read()
# file.write('sexy')

# with open("score.txt", 'r') as file:
#     score = file.read()
#     with open("score.txt", 'w') as file:
#         file.write(str(int(score)+1))

# for i in range(10):
#     with open(f"./letters/letter_for_{i}.txt", 'w') as file:
#         file.write(f'Hello {i}\n')

# Solutions
with open('./names/names.txt', 'r') as file:
    names = file.read().split("\n")
    # names = [i.strip('\n') for i in list(file)]
with open('./letters/sample_letter.txt') as file:
    sample_letter = file.read()

    print(names, sample_letter)

for name in names:
    with open(f'./letters/letter_to_{name}.txt', 'w') as file:
        file.write(sample_letter.replace('[name]', name))
