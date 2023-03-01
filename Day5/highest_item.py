sample_list = [int(i) for i in input("list elements").split()]

highest = 0
for item in sample_list:
    if item > highest:
        highest = item

print(highest)
