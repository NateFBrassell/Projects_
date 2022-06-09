pizzas = ['pepperoni', 'bacon', 'sausage']
for pizza in pizzas:
	print("I like " + pizza.title() + " pizza.")
	print("I really like " + pizza.title() + " pizza.")

print("I really love pizza!")

animals = ['dog', 'cat', 'fish']
for animal in animals:
	print("A " + animal.title() + " would make a great pet.")
print("Any of these animals would make a great pet for kids!")

print("\nThis is a my pizza and friends pizza list:")
my_pizzas = ['pepperoni', 'bacon', 'sausage']
print(my_pizzas)

friends_pizzas = ['pepperoni', 'bacon', 'sausage']
print(friends_pizzas)

my_pizzas.append('ham')
print(my_pizzas)

friends_pizzas.append('pineapple')
print(friends_pizzas)

for pizza in my_pizzas:
	print(my_pizzas)
    
for pizza in friends_pizzas:
	print(friends_pizzas)

