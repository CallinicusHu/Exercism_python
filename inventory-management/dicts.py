"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    inventory = dict.fromkeys(items)

    for word in inventory: #In line 13 inside create_inventory() (line 4), you are updating inventory as many times as there are 'items'. E. g. if 'wood' is present twice, you will .update({ 'wood': 2}) twice. Let's find a way to avoid updating the same mulitple times.
        numb = items.count(word)
        inventory.update({word: numb})

    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    for word in items:
        if not(word in inventory): #It will not necessarily be nicer or more understandable, but since you can give a default to .get() to return when the key is not present in the dict, you don't have to check for word in inventory before updating (on line 37).
            inventory.update({word: 0})
            #I don't understand where what how with .get?

    for word in items:
        plus = inventory.get(word)
        inventory.update({word: plus + 1})

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """

    for item in items: #Checking for key presence (line 57) doesn't seem to be important in the case of decrement_items().
        if not(item in inventory): #if I remove this the tests fail, because the loop resets all the values to 0.
            inventory.update({item: 0})

    for item in items:
        current_quantity_of_inventory = inventory.get(item)
        if current_quantity_of_inventory > 0:
            inventory.update({item: current_quantity_of_inventory -1})
    
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

    return listing

#But, commented out codes are notes and reminders for study. If I ever look back on the code I won't remember what I tried and failed and how.