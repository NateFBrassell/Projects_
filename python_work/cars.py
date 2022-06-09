cars = ['honda', 'chevy', 'kia', 'dodge']
print(cars)
message = "I would like to own a " + cars[0].title() + " SUV one day."
print(message)
message = "I would like to own a " + cars[1].title() + " SUV one day."
print(message)
message = "I would like to own a " + cars[2].title() + " SUV one day."
print(message)
message = "I would like to won a " + cars[3].title() + " SUV one day."
print(message)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# you can never revert back to original order of list, it goes alphabetical and stays that way.

cars.sort(reverse=True)
print(cars)
# .sort(reverse=True) makes your list result in backwards order alphabetically.

print("Here is the orginal list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# \n makes new line and sends message order has been sorted then shows example.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# >>> cars = ['bmw', 'audi','toyota', 'subaru']
# >>> len(cars)
#     4
# len() allows you to figure out the length of a list






