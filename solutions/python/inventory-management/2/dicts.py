"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """
    inventory = {}
    for item in items:
        if item not in inventory:
            inventory[item] = 1
        elif item in inventory:
            inventory[item]+= 1 
    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    Parameters:
        inventory (dict): Dictionary of existing inventory.
        items (list): List of items to update the inventory with.

    Returns:
        dict: The inventory updated with the new items.
    """
    inventory_updated = inventory.copy() 
    for item in items:
        if item not in inventory_updated:
            inventory_updated[item] = 1
        else:
            inventory_updated[item] += 1
    return inventory_updated
    


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    Parameters:
        inventory (dict): Inventory dictionary.
        items (list): List of items to decrement from the inventory.

    Returns:
        dict: Updated inventory with items decremented.
    """
    inventory_decremented = inventory.copy()
    for item in items:
        if item in inventory_decremented:
            if inventory_decremented[item] > 0:
                inventory_decremented[item] -= 1
    return inventory_decremented


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    Parameters:
        inventory (dict): Inventory dictionary.
        item (str): Item to remove from the inventory.

    Returns:
        dict: Updated inventory with item removed. Current inventory if item does not match.
    """
    inventory_cleared = inventory.copy()
    if item in inventory_cleared:
        inventory_cleared.pop(item)

    return inventory_cleared


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    Parameters:
        inventory (dict): An inventory dictionary.

    Returns:
        list[tuple]: List of key, value tuples from the inventory dictionary.
    """

    inventory_list = []
    for item in inventory:
        if inventory[item] > 0:
            new_item = (item, inventory[item])
            inventory_list.append(new_item)

    return inventory_list
