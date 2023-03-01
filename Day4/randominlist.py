import random

names = input('Add a list of names separate by a ","').split(',')
#print(names, len(names))
people = len(names)-1
print(names[random.randint(0, people)])
