for value in range(1,5):
   print(value)
   
for value in range(1,6):
	print(value)
# 0 start value applies here also.
	
	
numbers = list(range(1,6))
print(numbers)
# combining range() and list() function to make list of numbers.

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

squares = []
for value in range(1,11):
	squares.append(value**2)
	
print(squares)
# A cleaner way to print a list of values

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

