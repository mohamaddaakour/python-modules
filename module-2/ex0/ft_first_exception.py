def ft_first_exception(temp_str: int) -> None:
    try:
        temp_str = int(temp_str)

        print(f"Testing temperature: {temp_str}")

        if temp_str >= 0 and temp_str <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    except Exception:
        print(f"Testing temperature: {temp_str}")
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")

    print("")

    ft_first_exception("25")

    print("")

    ft_first_exception("abc")

    print("")

    ft_first_exception("100")

    print("")

    ft_first_exception("-50")

    print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
