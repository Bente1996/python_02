#!/usr/bin/env python3

from typing import Callable


class TemperatureTooHighException(Exception):
    pass


class TemperatureTooLowException(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise TemperatureTooLowException(f"Too cold ({temperature})")
    if temperature > 40:
        raise TemperatureTooHighException(f"Too warm ({temperature})")

    return temperature


def test_test_temperature(input: str) -> None:
    try:
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C")
    except ValueError as e:
        print(f"Caught input_temperature ValueError: {e}")
    except TemperatureTooHighException as e:
        print(f"Caught input_temperature TemperatureTooHighException: {e}")
    except TemperatureTooLowException as e:
        print(f"Caught input_temperature TemperatureTooLowException: {e}")
    except Exception as e:
        print(
            f"Caught input_temperature exception that wasn't recognized: {e}"
        )


def test_temperature() -> None:
    test_test_temperature("15")
    test_test_temperature("abc")
    test_test_temperature("100")
    test_test_temperature("-50")
    try:
        input = "25"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        input = "abc"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    try:
        input = "100"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")
    except TemperatureTooHighException as e:
        print(f"Caught input_temperature error: {e}")

    try:
        input = "-50"
        print(f"Input data is '{input}'")
        temperature = input_temperature(input)
        print(f"Temperature is now: {temperature}°C\n")
    except TemperatureTooLowException as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
