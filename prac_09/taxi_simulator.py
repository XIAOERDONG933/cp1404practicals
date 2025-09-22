from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    display_menu()
    choice = input(">>> ").lower()
    bill_amount = 0
    while choice != "q":
        if choice =="c":
            current_taxi = handle_choose_taxi(taxis)
        elif choice == "d":
            bill_amount += handle_drive(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_amount:.2f}")
        display_menu()
        choice = input(">>> ").lower()
    print(f"Total bill cost: ${bill_amount:.2f}")
    print(f"Taxis are now: ")
    display_available_taxis(taxis)


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
        current_taxi.start_fare()
        current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare

def display_available_taxis(taxis):
    """Display the available taxis."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def handle_choose_taxi(taxis):
    """Choose a taxi"""
    print("Taxis available: ")
    display_available_taxis(taxis)
    choice = int(input("Choose taxi: "))
    if choice < 0 or choice >= len(taxis):
        print("Invalid taxi choice")
    else:
        return taxis[choice]


main()