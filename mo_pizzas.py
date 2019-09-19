available_toppings = ["mushrooms", 'cheese', 'pepperoni', 'sausage']


requested_toppings = ['mushrooms', 'cheese', 'french fries']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else: 
		print(f"Sorry we do not have {requested_topping}")

print('\nPizza is done!')
