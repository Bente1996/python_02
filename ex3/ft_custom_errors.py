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
    if plant_name == "Potato":
        raise GardenError(f"Garden doesn't contain plant ({plant_name})")
    if days_old > 400:
        raise PlantError(f"Plant is too old, its wilting ({days_old}")
    if water_content < 100:
        raise WaterError("Plant doesnt have enough water, its dying")
    if water_content > 400:
        raise WaterError("Plant has too much water, its drowning")
    raise GardenError

def ft_custom_errors(name: str, days: int, water: int) -> None:
    try:
        harvest(name, days, water)
    except PlantError as e:
        print(f"plant {e}")
    except WaterError as e:
        print(f"water {e}")
    except GardenError as e:
        print(f"garden {e}")
    except Exception as e:
        print(f"some other error {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    ft_custom_errors("Potato", 100, 200)
    ft_custom_errors("cauliflower", 500, 200)
    ft_custom_errors("cauliflower", 300, 99)
    ft_custom_errors("cauliflower", 300, 401)
    ft_custom_errors("cauliflower", 300, 400)
