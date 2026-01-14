def ft_first_exception(temp_str):
    try:
        temp_str = int(temp_str)

        if temp_str >= 0 and temp_str <= 40:
            print(f"Temperature {temp_str}°C is perfect for plants!")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    except:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")

    ft_first_exception("25")
    ft_first_exception("abc")
    ft_first_exception("100")
    ft_first_exception("-50")

    print("All tests completed - program didn't crash!")

test_temperature_input()
