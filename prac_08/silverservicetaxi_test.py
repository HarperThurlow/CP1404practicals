from prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)
    print(hummer)
    print(hummer.current_fare_distance)
    print(hummer.get_fare())


main()
