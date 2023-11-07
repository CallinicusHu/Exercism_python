"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = dict.fromkeys(items)

    for word in items:
        numb = items.count(word)
        inventory.update({word: numb})

    #print("create inventory", inventory)

    return inventory



#x = create_inventory(["macs", "macs", "ka", "ma", "ma", "macs", "macs"])
#y = x
#print("x", x)
#print("y", y)

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for word in items:
        if not(word in inventory):
            inventory.update({word: 0})

    for word in items:
        plus = inventory.get(word)
        inventory.update({word: plus + 1})

    #print("add inventory", inventory)
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items:
        if not(item in inventory):
            inventory.update({item: 0})

    for item in items:
        current_quantity_of_inventory = inventory.get(item)
        if current_quantity_of_inventory > 0:
            inventory.update({item: current_quantity_of_inventory -1})
    

    print(inventory)
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """

    if item in inventory:
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    """
    listing = list(inventory)

    print("\n", listing)
    print(len(inventory))

    for next in range(len(inventory)):
        listing.insert(next * 2, )

    print("\n", listing)

    """

    new_inventory = inventory.copy()

    for item in inventory:
        if inventory.get(item) == 0:
            new_inventory.pop(item)

    listing = list(new_inventory.items())

    #listing = list(listing)

    return listing
