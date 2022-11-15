person_height = int(input("How tall are you in cm?"))/100
person_weight = int(input("How much you weigh in kg?"))
bmi = round(person_weight/(person_height**2))
bmi_range = "normal_weight"
if bmi < 18.5:
    bmi_range = "underweight"
elif bmi < 25:
    bmi_range = "normal_weight"
elif bmi < 30:
    bmi_range = "overweight"
elif bmi < 35:
    bmi_range = "obese"
else:
    bmi_range = "clinically obese"

#print(person_weight, person_height)
print("BMI:", bmi, bmi_range)
