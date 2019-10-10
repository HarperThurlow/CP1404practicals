from prac_08.unreliablecar import UnreliableCar


def main():

    bad_car = UnreliableCar("Bad", 100, 50)
    for i in range(10):
        bad_car.drive(10)
        print(bad_car.odometer)


main()
