"""
Prac 01 - Loops

"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

amount_of_stars = int(input("How many stars? >"))

for i in range(0, amount_of_stars):
    print("*", end='')
print()

count = 1
for i in range(0, amount_of_stars):
    print("*" * count, end='\n')
    count += 1
print()
