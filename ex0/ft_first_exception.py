#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature

def test_temperature() -> None:
    try:
        input = "25"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")

        input = "abc"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")

    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with"
              f" base 10: '{input}'\n")

    print("All tests completed - program didn't crash")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
