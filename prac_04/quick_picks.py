from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 45
MAX_PICKS = 6


def main():

    lines = int(input("How many lines? >"))
    while lines <= 0:
        print("Please enter a valid number of lines")
        lines = int(input("How many lines? >"))

    for line in range(lines):
        quick_pick = []
        for i in range(MAX_PICKS):
            number = randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_pick:
                number = randint(MIN_NUMBER, MAX_NUMBER)
            quick_pick.append(number)
        quick_pick.sort()

        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
