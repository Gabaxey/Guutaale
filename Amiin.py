# item  one   

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
#  list four
items = ["item1" , "item2" , "item3"]
quantities = [quantity1 , quantity2 , quantity3]
prices = [price1 , price2 , price3]

# dictionary 5
furo = ('quantity' , 'price')

# six
store = {
    item1: { furo[0]:quantities[0], furo[1]:prices[0]},
    item2: { furo[0]:quantities[1], furo[1]:prices[1] },
    item3: { furo[0]:quantities[2], furo[1]:prices[2] },
    
}
# # Calculate total value for each item
total_value_item1 = quantity1*price1
total_value_item2 = quantity2*price2
total_value_item3 = quantity3*price3

totals = total_value_item1+total_value_item2+total_value_item3

print("n---------Amiin------")
print(item1,store[item1][furo[0]],  store[item1][furo[1]])
print('total voalue item one' ,total_value_item1 )


