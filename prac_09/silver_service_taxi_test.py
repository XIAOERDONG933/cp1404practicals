"""
CP1404/CP5632 Practical
silver service taxi test
"""
from silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi"""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    standard = SilverServiceTaxi("Standard", 100, 2)

    # Test initial state
    print("Initial state:")
    print(hummer)
    print(standard)
    print()

    # Test fare calculation
    print("Fare tests:")
    hummer.drive(10)
    print(f"Hummer after 10km: {hummer}")
    print(f"Fare: ${hummer.get_fare():.2f}")

    standard.drive(18)
    print(f"Standard after 18km: {standard}")
    print(f"Fare: ${standard.get_fare():.2f}")

    # Assert tests
    print("\nRunning assert tests...")
    # Test fanciness of 2 with 18km trip = (1.23 * 2 * 18) + 4.50 = 48.78
    standard.start_fare()  # Reset fare
    standard.drive(18)
    assert round(standard.get_fare(), 2) == 48.78, "Fare for 18km with fanciness 2 should be $48.78"

    # Test fanciness of 4 with 10km trip = (1.23 * 4 * 10) + 4.50 = 53.70
    hummer.start_fare()  # Reset fare
    hummer.drive(10)
    assert round(hummer.get_fare(), 2) == 53.70, "Fare for 10km with fanciness 4 should be $53.70"

    print("All assert tests passed!")

if __name__ == "__main__":
    main()