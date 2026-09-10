#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str="Unknown GardenError") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str="Unknown PlantError") -> None:
        super().__init__(message)

def check_capital(plant_name: str) -> bool:
    if plant_name[0] >= 'A' and plant_name[0] <= 'Z':
        return True
    return False

def water_plant(plant_name: str, valid: bool) -> None:
    if valid:
        plant_name = str.capitalize(plant_name)
    if check_capital(plant_name) is False:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering ({plant_name}): [OK]")


def test_watering_system(valid: bool) -> None:
    print("Opening water system")
    try:
        water_plant("Tomato", valid)
        water_plant("lettuce", valid)
        water_plant("carrots", valid)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("..ending tests and returing to main")
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    test_watering_system(True)
    print("\nTesting invalid plants...")
    test_watering_system(False)
