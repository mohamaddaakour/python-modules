# ft_inventory_system.py
import sys


def parse_inventory(args):
    """Parse command line args like sword:1 potion:5 ... into a dictionary"""
    inventory = dict()
    for arg in args:
        if ':' in arg:
            name, qty = arg.split(':')
            inventory[name] = int(qty)
    return inventory


def inventory_summary(inventory):
    # calculate total items manually
    total_items = 0
    for qty in inventory.values():
        total_items += qty

    unique_items = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print("")

    # === Current Inventory ===
    # sort manually by quantity descending
    items_list = list(inventory.items())
    for i in range(len(items_list)):
        for j in range(i+1, len(items_list)):
            if items_list[j][1] > items_list[i][1]:
                items_list[i], items_list[j] = items_list[j], items_list[i]

    print("=== Current Inventory ===")
    for item, qty in items_list:
        pct = (qty / total_items) * 100
        unit = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit} ({pct:.1f}%)")
    print("")

    # === Inventory Statistics ===
    most_item = None
    least_item = None
    for item, qty in inventory.items():
        if most_item is None or qty > most_item[1]:
            most_item = (item, qty)
        if least_item is None or qty < least_item[1]:
            least_item = (item, qty)
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} units)")
    print("")

    # === Item Categories ===
    moderate = dict()
    scarce = dict()
    for item, qty in inventory.items():
        if qty >= 4:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print("=== Item Categories ===")
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print("")

    # === Management Suggestions ===
    restock = []
    for item, qty in inventory.items():
        if qty <= 1:
            restock.append(item)
    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")
    print("")

    # === Dictionary Properties Demo ===
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main():
    args = sys.argv[1:]
    inventory = parse_inventory(args)
    inventory_summary(inventory)


if __name__ == "__main__":
    main()
