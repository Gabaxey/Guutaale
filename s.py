# item one
item1 = "shaati"
item2 = "surwaal"
item3 = "fanaanad"

# quantity two
quantity1 = 30
quantity2 = 40
quantity3 = 60

# price three
price1 = 10.5
price2 = 9.6
price3 = 5

# dictionary keys (quantity, price)
furo = ('quantity', 'price')

# six - store dictionary
store = {
    item1: { furo[0]: quantity1, furo[1]: price1 },
    item2: { furo[0]: quantity2, furo[1]: price2 },
    item3: { furo[0]: quantity3, furo[1]: price3 },
}

# Calculate total value for each item
total_value_item1 = quantity1 * price1
total_value_item2 = quantity2 * price2
total_value_item3 = quantity3 * price3

# Calculate overall total
totals = total_value_item1 + total_value_item2 + total_value_item3

# Output the totals
print("\n--- Inventory ---")
for item in [item1, item2, item3]:
    quantity = store[item][furo[0]]
    price = store[item][furo[1]]
    total_value = quantity * price
    print(f"Item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price: {price}")
    print(f"Total value: {total_value}")
    print("-" * 20)

# Display the total value of the inventory
print(f"Total value of the entire inventory: {totals}")
