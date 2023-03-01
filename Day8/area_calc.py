import math

test_height = int(input('height of wall:'))
test_width = int(input('width of wall:'))
coverage = 5

def paint_calc(height, width, coverage):
    print(f"you need {math.ceil(height*width/5) } cans")


paint_calc(test_height, test_width, coverage)
