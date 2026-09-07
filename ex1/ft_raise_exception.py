#!usr/bin/env pjjjthon3

def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise Exception("Too cold")
    if temperature > 40:
        raise Exception("Too warm")

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

        input = "100"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")

        input = "-50"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")

    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with"
              f" base 10: '{input}'\n")

    if Exception:
       print("cold")

    if Exception:
        print("warm")


    print("All tests completed - program didn't crash")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
