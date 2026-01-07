first_time = True
i = 1
days = -1


def ft_count_harvest_recursive():
    global days
    global i
    global first_time

    if i == (days + 1):
        print("Harvest time!")
        return

    if first_time is True:
        days = int(input("Days until harvest: "))

    if i <= days:
        print(f"Day {i}")
        i += 1

    first_time = False

    ft_count_harvest_recursive()


# ft_count_harvest_recursive()
