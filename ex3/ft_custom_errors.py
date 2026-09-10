#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str="Unknown GardenError") -> None:
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message: str="Unknown PlantError") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str="Unknown WaterError") -> None:
        super().__init__(message)

def harvest(plant_name: str, days_old: int, water_content: int) -> None:
    if plant_name == "potato":
        raise GardenError(f"Garden doesn't contain plant ({plant_name})")
    if days_old < 100:
        raise PlantError(f"Plant ({plant_name}) is too young to harvest"
                         f" ({days_old} days)")
    if days_old > 400:
        raise PlantError(f"Plant ({plant_name}) is too old, it's wilting"
                         f" ({days_old} days)")
    if water_content < 100:
        raise WaterError(f"Plant ({plant_name}) doesn't have enough water"
                         f" ({water_content}), it's dying")
    if water_content > 400:
        raise WaterError(f"Plant ({plant_name}) has too much water"
                         f" ({water_content}), it's drowning")
    if plant_name == "garden":
        raise GardenError
    if plant_name == "plant":
        raise PlantError
    if plant_name == "water":
        raise WaterError
    raise Exception("pluh")

def ft_custom_errors(name: str, days: int, water: int) -> None:
    try:
        harvest(name, days, water)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

def garden_errors(name: str, days: int, water: int) -> None:
    try:
        harvest(name, days, water)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    except Exception as e:
        print(f"Caught an error: {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    ft_custom_errors("cauliflower", 500, 200)
    ft_custom_errors("plant", 300, 300)
    print("\nTesting WaterError...")
    ft_custom_errors("cauliflower", 300, 99)
    ft_custom_errors("cauliflower", 300, 401)
    ft_custom_errors("water", 300, 300)
    print("\nTesting catching all garden errors...")
    garden_errors("potato", 300, 300)
    garden_errors("cauliflower", 500, 200)
    garden_errors("cauliflower", 300, 99)
    garden_errors("cauliflower", 300, 401)
    garden_errors("garden", 300, 300)
    garden_errors("plant", 300, 300)
    garden_errors("water", 300, 300)
    garden_errors("perfect_plant", 300, 300)
    print("\nAll custom error types work correctly")
