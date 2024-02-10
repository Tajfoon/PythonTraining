# Write a Python script that does the following:
#
# - Prints out a “banner” to welcome users to our shop
# - Asks the user for the name of the item they are buying
# - Asks the user for the price of that item
# - Asks the user for the quantity they are purchasing
# - Prints out a message that includes their subtotal (quantity 𝚡 price)
#
# **Here’s an example of the script running (the green text is user input)**


print('Welcome to our shop!')
item_name = input('Select item: ')
item_price = int(input('What is price: '))
item_quantity = int(input('Type how many want you buy:'))

print(f'')