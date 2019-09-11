from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
    print(gibson)
    another_guitar = Guitar("James B", 2005, 2051)
    print(another_guitar)

    print("{} get_age() - Expected 96. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Expected 14. Got {}".format(another_guitar.name, another_guitar.get_age()))

    print("{} is_vintage() - Expected True. Got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
