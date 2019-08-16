"""
Prac 02 - Files
Harper Thurlow
"""
# Part 1
out_file = open("name.txt", 'w')
name = input("What is your name? >")
print("{}".format(name), file=out_file)
out_file.close()

# Part 2
in_file = open("name.txt", 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

# Part 3
number_file = open("numbers.txt", 'r')
number_1 = number_file.readline()
number_2 = number_file.readline()
print(int(number_1) + int(number_2))
number_file.close()
# After checking solutions to see how Lindsay did it.
# CAN ADD int(file) to just get numbers

# Part 4
number_file = open("numbers.txt", 'r')
total = 0

for line in number_file:
    total += int(line)

print(total)
number_file.close()
