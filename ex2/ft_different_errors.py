#!/usr/bin/env python3

def garden_operations(operation_number: int) -> str | None:
    if operation_number == 0:
        return "abc"
    elif operation_number == 1:
        return "1"
    elif operation_number == 2:
        return "file.txt"
    elif operation_number == 3:
        return "a"
    elif operation_number == 4:
        return "2"
    return

def test_error_types(operation_number: int) -> None:
    input = garden_operations(operation_number)
    try:
        print(f"Input data is: {input}")
        if operation_number == 0:
            print(f"Value is now: {int(input)}")
            print("Operation completed succesfully")
        elif operation_number == 1:
            print(f"Value is now: {int(input)/0}")
            print("Operation completed succesfully")
        elif operation_number == 2:
            open(input)
            print("Operation completed succesfully")
        elif operation_number == 3:
            print(input + 1)
            print("Operation completed succesfully")
        elif operation_number == 4:
            print(int(input))
            print("Operation completed succesfully")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"CaughtZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")

if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_types(0)
    print("Testing operation 1...")
    test_error_types(1)
    print("Testing operation 2...")
    test_error_types(2)
    print("Testing operation 3...")
    test_error_types(3)
    print("Testing operation 4...")
    test_error_types(4)
    print("\nAll error types tested successfully!")
