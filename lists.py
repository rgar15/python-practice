# find numbers in commmon between 2 lists and print them

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elem in a:
    if elem in b and elem not in c:
        c.append(elem)
print(c)

