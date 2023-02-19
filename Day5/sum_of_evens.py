evens = []
for i in range(1, 101):
    print(i)
    if i % 2 == 0:
        evens.append(i)

print(sum(evens)/len(evens))
