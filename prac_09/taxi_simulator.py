from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    print("Let's drive!")
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    display_menu()
    choice = input(">>> ").lower()
    bill_amount = 0
    while choice != "q":
        if choice =="c":
            pass
        elif choice == "d":
            bill_amount += handle_drive(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_amount:.2f}")
        display_menu()
        choice = input(">>> ").lower()


def display_menu():
    """Display the menu."""
    print("q)uit, c)hoose taxi, d)rive")


def handle_drive(current_taxi):
    """Drive the taxi"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    else:
        distance = int(input("Drive how far? "))
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        current_taxi.start_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare

main()