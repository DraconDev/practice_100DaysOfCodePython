student_heights = input('height').split()

print(student_heights)
sum_height = 0
count = 0

for height in student_heights:
    print(height)
    sum_height += int(height)
    count += 1

print(sum_height, sum_height/count)
