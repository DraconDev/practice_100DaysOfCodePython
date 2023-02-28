list = [1, 2, 3]
names = ["Angela", "Bob", "Freddy", "Sammy", 'Jack']
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# test = [i + 1 for i in list]
# test = [i for i in 'Angela']
# test = [i*2 for i in range(1, 5)]
# test = [i*2 for i in list if i < 3]
# test = [i.upper() for i in names if len(i) > 4]
# test = [i * i for i in numbers]
test = [i for i in numbers if i % 2 == 0]


print(test)
