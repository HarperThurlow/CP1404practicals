from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    bill_to_date = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(MENU)
    option = input(">>>").upper()
    while option != "Q":
        if option == "C":
            current_taxi = choose_taxi(taxis)
            print(current_taxi)
        elif option == "D":
            trip_cost = drive_taxi(current_taxi)
            bill_to_date += trip_cost
        else:
            print("Invalid option")

        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        option = input(">>>").upper()
    print("Total trip cost: ${}\nTaxis are now:".format(bill_to_date))
    print_taxis(taxis)


def choose_taxi(taxis):
    print_taxis(taxis)
    taxi_choice = int(input("Choose taxi: "))
    return taxis[taxi_choice]


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def drive_taxi(current_taxi):
    if current_taxi is None:
        print("Please choose a taxi first")
        return 0
    current_taxi.start_fare()
    drive_distance = int(input("Drive how far? "))
    current_taxi.drive(drive_distance)
    print("Your {} trip cost you ${}".format(current_taxi.name, current_taxi.get_fare()))
    return current_taxi.get_fare()


main()
