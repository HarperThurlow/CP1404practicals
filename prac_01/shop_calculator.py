"""
Prac 01 - shop calculator

"""

number_of_items = int(input("How many items: "))

while number_of_items <= 0:
    print("invalid number of items")
    number_of_items = int(input("How many items: "))
total = 0
price = 0
for i in range(number_of_items):
    price = int(input("Price of Item:"))
    total += price
    price = 0

print("Total price for", number_of_items, "items is: $", total)
