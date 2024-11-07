# Step 1: Define the items in the inventory
item1 = "Apples"
item2 = "Bananas"
item3 = "Oranges"
#
quantity1 = 30
quantity2 = 40 
quantity3 = 60 
 
 # price three
price1 = 10.5
price2 = 9.6
price3 = 5

# Step 4: Create lists to store items, quantities, and prices
items = [item1, item2, item3]
quantities = [quantity1, quantity2, quantity3]
prices = [price1, price2, price3]

# Step 5: Create a dictionary to store each item's quantity and price
inventory = {
    item1: {"quantity": quantity1, "price": price1},
    item2: {"quantity": quantity2, "price": price2},
    item3: {"quantity": quantity3, "price": price3}
}

# Step 6: Calculate the total value of each item (quantity * price)
total_value_item1 = inventory[item1]["quantity"] * inventory[item1]["price"]
total_value_item2 = inventory[item2]["quantity"] * inventory[item2]["price"]
total_value_item3 = inventory[item3]["quantity"] * inventory[item3]["price"]

# Step 7: Calculate the total value of the entire inventory
total_inventory_value = total_value_item1 + total_value_item2 + total_value_item3

# Step 8: Display the results
print("\n--- Inventory ---")
print("Item: ", item1)
print("Quantity: ", inventory[item1]["quantity"])
