# new_dict = {new_key:new_value for item in list}

# lists
import random

list = [1, 2, 3]
names = ["Angela", "Bob", "Freddy", "Sammy", 'Jack']
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
dictionary = {'a': 1, 'b': 2, "c": 2}
student_scores = {k: random.randint(1, 100) for k in names}
sentence = "What is the airspeed velocity of an unladen swallow"
day_temperature = {'Monday': 23, "Tuesday": 12}

# print(student_scores)

# test = {i: i for i in names}
# test = {k: v for (k, v) in dictionary.items()}
# test = {k: v for (k, v) in dictionary.items() if v == 2}
# test = {k: v for (k, v) in dictionary.items() if v == 2 if k == "b"}
# test = {k: v if v > 1 else False for (k, v) in dictionary.items()}
# test = {k: (v if v > 1 else False) for (k, v) in dictionary.items()}
# test = {k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)}
# test = {k: v for k, v in student_scores.items()}
# test = {k: v for k, v in student_scores.items() if v > 60}
# test = {k: len(k) for k in sentence.split(' ')}
test = {day: temperature*1.8+32 for day, temperature in day_temperature.items()}


# test = dictionary

print(test)
