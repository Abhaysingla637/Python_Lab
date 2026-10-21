def display_inventory(store, inventory):
    print(f"\n{store} Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


def merge_inventory(*stores):
    merged = {}
    for inventory in stores:
        merged |= inventory
    return merged


def total_stock(inventory):
    return {
        item: sum(store.get(item, 0) for store in inventory)
        for item in set().union(*(store.keys() for store in inventory))
    }


def check_stock(inventory, item):
    if item in inventory:
        print(f"{item}: {inventory[item]} units available")
    else:
        print(f"{item} is not in the inventory.")


def main():
    store1 = {"Pen": 20, "Notebook": 15, "Pencil": 30}
    store2 = {"Pen": 10, "Eraser": 12, "Notebook": 8}
    store3 = {"Pencil": 15, "Eraser": 5, "Ruler": 10}

    display_inventory("Store 1", store1)
    display_inventory("Store 2", store2)
    display_inventory("Store 3", store3)

    stores = [store1, store2, store3]
    combined = total_stock(stores)

    print("\nCombined Inventory:")
    for item, quantity in combined.items():
        print(f"{item}: {quantity}")

    check_stock(combined, "Pen")
    check_stock(combined, "Marker")


if __name__ == "__main__":
    main()
