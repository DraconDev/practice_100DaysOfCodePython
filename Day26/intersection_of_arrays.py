import pandas

test = ''

with open('./data.txt') as file:
    with open('./data2.txt') as file2:
        array1 = file.read().split('\n')
        array2 = file2.read().split('\n')
        # sets
        # intersection = set(array1).intersection(set(array2))
        intersection = [int(i) for i in array1 if i in array2 and i != '']


test = intersection

print(test)
