def ft_garden_summary():
    name = input("Enter garden name: ")
    plants_num = int(input("Enter number of plants: "))

    print(f"Garden: {name}")
    print(f"Plants: {plants_num}")

    if plants_num < 15:
        status = "You are in the right way"
    elif plants_num >= 15 and plants_num < 25:
        status = "Good job you are so close"
    else:
        status = "Growing well!!"

    print(f"Status: {status}")

# ft_garden_summary()
