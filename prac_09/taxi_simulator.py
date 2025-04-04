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
    while choice != "q" and choice != "quit":
        if choice =="c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_amount:.2f}")
        display_menu()
        choice = input(">>> ").lower()


def display_menu():
    """Display the menu."""
    print("q)uit, c)hoose taxi, d)rive")



main()