first_persons_name = input("First persons name?").lower()
second_persons_name = input("Second persons name?").lower()
names = first_persons_name + second_persons_name

print(names)

count_true = names.count('t') + names.count('r') + \
    names.count('u') + names.count('e')
count_love = names.count('l') + names.count('o') + \
    names.count('v') + names.count('e')

love_compatibility = int(str(count_true)+str(count_love))

print(count_true, count_love, type(love_compatibility))


def output(love_percentage):
    if love_percentage > 89:
        print('Amazing compatibility')
    elif love_percentage >= 30 and love_percentage <= 70:
        print("Decent compatibility")
    else:
        print(F"{love_percentage}% Love compatibility")


output(love_compatibility)
