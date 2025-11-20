"""
CP1404/CP5632 Practical
unreliable car test
"""
from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class with single and multiple drive attempts."""

    # Create cars with different reliabilities
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 30)

    # Test 1: Single drive attempt
    print("Single drive test:")
    print(f"Before: {reliable_car}")
    distance = reliable_car.drive(50)
    print(f"After driving 50km (90% reliable): {reliable_car}, drove {distance}km")
    print(f"Before: {unreliable_car}")
    distance = unreliable_car.drive(50)
    print(f"After driving 50km (30% reliable): {unreliable_car}, drove {distance}km")
    print()

    # Test 2: Multiple drive attempts to demonstrate reliability
    print("Multiple drive test (100 attempts of 10km each):")
    reliable_success = 0
    unreliable_success = 0
    attempts = 100

    for i in range(attempts):
        # Reset fuel and odometer for consistent testing
        reliable_car.fuel = 100
        reliable_car.odometer = 0
        unreliable_car.fuel = 100
        unreliable_car.odometer = 0

        # Count successful drives
        if reliable_car.drive(10) > 0:
            reliable_success += 1
        if unreliable_car.drive(10) > 0:
            unreliable_success += 1

    # Calculate and display success rates
    reliable_rate = reliable_success / attempts * 100
    unreliable_rate = unreliable_success / attempts * 100

    print(f"Reliable car (90%) succeeded {reliable_success} times ({reliable_rate:.1f}%)")
    print(f"Unreliable car (30%) succeeded {unreliable_success} times ({unreliable_rate:.1f}%)")


if __name__ == "__main__":
    main()