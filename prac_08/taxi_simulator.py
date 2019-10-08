from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    option = input(">>>").upper()
    while option != "Q":
        if option == "C":
            choose_taxi()
        elif option == "D":
            drive_taxi()
        else:
            print("Invalid option")


def choose_taxi():
    pass


def drive_taxi():
    pass
