"""Harper Thurlow"""

MIN_LENGTH = 5

password = input("Please enter a password longer than {} >".format(MIN_LENGTH))

while len(password) <= MIN_LENGTH:
    password = input("Please enter a password longer than {} >".format(MIN_LENGTH))

print(len(password) * "*")
