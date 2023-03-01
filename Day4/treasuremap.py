row1 = [0, 0, 0]
row2 = [0, 0, 0]
row3 = [0, 0, 0]

map = [row1, row2, row3]

print(f"   1  2  3 \n1 {map[0]}\n2 {map[1]}\n3 {map[2]}\n")

position = list(input("Where do you want to put the treasure?").lower())
position = [int(x) for x in position]
print(position)
map[position[0]-1][position[1]-1] = "X"
print(f"   1  2  3 \n1 {map[0]}\n2 {map[1]}\n3 {map[2]}\n")
