from prac_08.unreliablecar import UnreliableCar


def main():
    bad_car = UnreliableCar("Bad", 100, 25)
    bad_car.drive(50)
    print(bad_car.odometer)


main()
