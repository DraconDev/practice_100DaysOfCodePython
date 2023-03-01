test = ['a\n', 'b\n', 'c\n', 'd\n', 'e\n', 'f\n', 'g\n', 'h\n', 'i\n', 'l']

# No mutation

for name in test:
    name = name.strip("\n")
# 
# Mutates

test = [i.strip('\n') for i in test]

# for i in range(len(test)):
#     test[i] = test[i].strip("\n")

# for name in enumerate(test):
#     print(name)
#     test[name[0]] = name[1].strip("\n")


print(test)
