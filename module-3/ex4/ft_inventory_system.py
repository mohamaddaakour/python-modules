def calculate_inventory_value(inventory):
    total = 0
    for item in inventory.values():
        total += item["quantity"] * item["value"]
    return total


def count_items(inventory):
    total = 0
    for item in inventory.values():
        total += item["quantity"]
    return total


def category_summary(inventory):
    categories = dict()
    for item in inventory.values():
        category = item["category"]
        categories[category] = categories.get(category, 0) + item["quantity"]
    return categories


def print_inventory(name, inventory):
    print(f"=== {name}'s Inventory ===")
    for item_name, data in inventory.items():
        total_price = data["quantity"] * data["value"]
        print(
            f"{item_name} ({data['category']}, {data['rarity']}): "
            f"{data['quantity']}x @ {data['value']} gold each = {total_price} gold"
        )

    value = calculate_inventory_value(inventory)
    items = count_items(inventory)
    categories = category_summary(inventory)

    print(f"Inventory value: {value} gold")
    print(f"Item count: {items} items")

    category_line = []
    for cat, qty in categories.items():
        category_line.append(f"{cat}({qty})")
    print("Categories: " + ", ".join(category_line))


def main():
    print("=== Player Inventory System ===")

    alice = dict({
        "sword": {"quantity": 1, "category": "weapon", "rarity": "rare", "value": 500},
        "potion": {"quantity": 5, "category": "consumable", "rarity": "common", "value": 50},
        "shield": {"quantity": 1, "category": "armor", "rarity": "uncommon", "value": 200},
    })

    bob = dict({
        "potion": {"quantity": 0, "category": "consumable", "rarity": "common", "value": 50},
        "magic_ring": {"quantity": 1, "category": "accessory", "rarity": "rare", "value": 300},
    })

    print_inventory("Alice", alice)

    print("=== Transaction: Alice gives Bob 2 potions ===")
    if alice.get("potion")["quantity"] >= 2:
        alice["potion"]["quantity"] -= 2
        bob["potion"]["quantity"] += 2
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    print("=== Updated Inventories ===")
    print(f"Alice potions: {alice.get('potion')['quantity']}")
    print(f"Bob potions: {bob.get('potion')['quantity']}")

    print("=== Inventory Analytics ===")

    alice_value = calculate_inventory_value(alice)
    bob_value = calculate_inventory_value(bob)

    if alice_value >= bob_value:
        print(f"Most valuable player: Alice ({alice_value} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_value} gold)")

    alice_items = count_items(alice)
    bob_items = count_items(bob)

    if alice_items >= bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")

    rare_items = []
    for name, data in alice.items():
        if data["rarity"] == "rare":
            rare_items.append(name)
    for name, data in bob.items():
        if data["rarity"] == "rare":
            rare_items.append(name)

    print("Rarest items: " + ", ".join(rare_items))


if __name__ == "__main__":
    main()
