def garden_operations():
    print("=== Garden Error Types Demo ===")

    print("")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("")

    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt") as f:
            pass
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("")

    print("Testing KeyError...")
    garden_plants = {"rose": 5, "sunflower": 3}
    try:
        count = garden_plants["missing_plant"]
        print(count)
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("")

    print("Testing multiple errors together...")
    try:
        x = int("xyz")
        y = 1 / 0
        print(x)
        print(y)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Caught an error, but program continues!")


def test_error_types():
    garden_operations()
    print("")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
