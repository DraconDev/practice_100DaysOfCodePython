person_height = int(input("How tall are you in cm?"))/100
person_weight = int(input("How much you weigh in kg?"))

print(person_weight, person_height)
print("BMI:", person_weight/(person_height**2))  