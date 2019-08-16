"""Harper Thurlow"""


def main():
    password = get_password()
    get_asterisks(password)


def get_asterisks(password):
    print(len(password) * "*")


def get_password():
    min_length = 5
    password = input("Please enter a password longer than {} >".format(min_length))
    while len(password) <= min_length:
        password = input("Please enter a password longer than {} >".format(min_length))
    return password


main()
