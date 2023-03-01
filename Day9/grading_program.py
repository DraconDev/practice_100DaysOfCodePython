student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "5"
    elif student_scores[key] > 80:
        student_grades[key] = "4"
    elif student_scores[key] > 70:
        student_grades[key] = "3"
    elif student_scores[key] > 60:
        student_grades[key] = "2"
    else:
        student_grades[key] = "fail"

print(student_grades)
