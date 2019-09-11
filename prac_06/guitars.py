from prac_06.guitar import Guitar


def main():
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        print("{} added.".format(new_guitar))
        guitars.append(new_guitar)
        name = input("Name: ")

    print("These are my Guitars:")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage = "(vintage)"
        else:
            vintage = ""
        print("Guitar {}: {} ({}), worth ${} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage))


main()
