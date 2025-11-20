"""
CP1404/CP5632 Practical taxi simulator
Estimate: 60 minutes
Actual:   82 minutes
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Coordinates all functions"""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    choice = ''
    while choice != 'q':
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'c':
            current_taxi = choose_taxi(taxis)
            display_bill(total_bill)
        elif choice == 'd':
            trip_cost = drive_taxi(current_taxi)
            total_bill += trip_cost
            display_bill(total_bill)
        elif choice != 'q':
            print("Invalid option")
            display_bill(total_bill)

    display_final_state(taxis, total_bill)

def display_taxis(taxis):
    """Display all available taxis"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    """Let user choose a taxi and return the selected taxi"""
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            selected_taxi = taxis[taxi_choice]
            selected_taxi.start_fare()
            return selected_taxi
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None

def drive_taxi(current_taxi):
    """Process taxi driving and return trip cost"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0
    try:
        distance = int(input("Drive how far? "))
        if distance > 0:
            distance_driven = current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} drove {distance_driven}km and trip cost you ${trip_cost:.2f}")
            return trip_cost
        else:
            print("Distance must be positive")
            return 0.0
    except ValueError:
        print("Invalid distance")
        return 0.0

def display_bill(total_bill):
    """Display current total bill"""
    print(f"Bill to date: ${total_bill:.2f}")

def display_final_state(taxis, total_bill):
    """Display final state and total bill"""
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")



if __name__ == '__main__':
    main()