def calc_total_price(product_price, quantity):
	return product_price * quantity


print('enter product name:')
product_name = input('')
print('enter product price:')
product_price = input('')
print('enter quantity')
quantity = input('')
print(product_name, product_price, quantity)
print('''the product name is: %s, 
	the product price is: %s, 
	the quantity is: %s''' % (product_name, product_price, quantity))
product_price = float(product_price)
quantity = int(quantity)
total_price = calc_total_price(product_price, quantity)
print('total_price is: ', total_price)



