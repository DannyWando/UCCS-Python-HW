"""
Homework 3, Exercise 3
Daniel Wandeler

This program is an inventory database, which can print the entire inventory to the console.
It also allows the user to add and delete products at any time.
"""

def printInventory(inventory):
    header1 = 'Product'
    header2 = 'Quantity'
    print(f'{header1:20} {header2:10}')
    for product, amount in inventory.items():
        print(f'{product:15} {amount:10}')


def addItem(inventory, item):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
    print('A product has been added to the inventory.')


def deleteItem(inventory,item):
    if item in inventory and inventory[item] == 1:
        del inventory[item]
        print('A product has been fully deleted from the inventory.')
    elif item in inventory and inventory[item] > 1:
        inventory[item] -= 1
        print('A product has been deleted from the inventory.')
    else:
        print('The product could not be found in the inventory.')


if __name__ == '__main__':
    sampleInventory = {
        'Hand sanitizer': 10,
        'Soap': 6,
        'Kleenex': 22,
        'Lotion': 16,
        'Razors': 12
    }
    printInventory(sampleInventory)

    #Testing to verify that addItem and deleteItem are working
    addItem(sampleInventory, 'Soap')
    addItem(sampleInventory, 'Lotion')
    addItem(sampleInventory, 'Razors')
    deleteItem(sampleInventory, 'Kleenex')
    deleteItem(sampleInventory, 'Hand sanitizer')
    printInventory(sampleInventory)
