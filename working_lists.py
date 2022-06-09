magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
	
	print("Thank you everyone, that was a great magic show!")
	
	
for value in range(1,6):
	print(value)
	
	
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	
print(squares)


digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))

print(max(digits))

print(sum(digits))


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
	
	
	
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends's favorite foods are:")
print(friend_foods)
	
	
	
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])


dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)
	
	
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
	
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)
	

	
	

