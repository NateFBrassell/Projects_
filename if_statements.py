# simple example of if statement in python.


drinks = ['pop', 'beer', 'gatorade', 'water']

for drink in drinks:
	if drink == 'beer':
		print(drink.upper())
	else:
		print(drink.title())


# Checking for Inequality in python using if statement.
requested_topping = 'pepperoni'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")
	
	
answer = 21

if answer != 32:
	print("That is not the correct answer. Please try again!")
	
	
	
# Checking Wheter a Value is not in a list.
banned_users = ['andrew', 'carolina', 'david']
user = 'andrew'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")
	
else:
	print("You cannot make a response, you are BANNED!")
	
	
# Simple if statements.
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
	
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
	
# The if-elif-else Chain.
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
	
	
age = 28

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
	
print("Your admission cost is $" + str(price) + ".")

# Testing multiple conditions
requested_toppings = ['light sauce', 'extra cheese', 'double pepperoni']

if 'light sauce' in requested_toppings:
	print("Adding light sauce.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
if 'double pepperoni' in requested_toppings:
	print("Adding double pepperoni.")
if 'onions' in requested_toppings:
	print("Adding onions.")
	
print("\nFinished making your pizza!")


# Using if statements with lists, checking for special items.
requested_toppings = ['light sauce', 'green peppers', 'double pepperoni', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
		
print("\nFinished making your pizza!")


# Checking that a list is not empty.
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
	
else:
	print("Are you sure you want a plain pizza?")
	
	
# Using multiple lists.
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
		
print("\nFinished making your pizza!")
	
	
	

