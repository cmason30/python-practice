hamburger = {
	'bun': 'wheat',
	'toppings': ['tomato', 'lettuce', 'cheese'],
	'exclusions': ['pickles', 'onion', 'bacon'],
}

print(f"You ordered a {hamburger['bun']} bun burger with"
	"the following toppings:")

for topping in hamburger['toppings']:
	print("\t" + topping)

print("...and the following will be excluded from the order:")

for exclusion in hamburger['exclusions']:
	print("\t" + exclusion)