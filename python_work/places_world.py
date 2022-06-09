places = ['jamaica', 'ireland', 'denmark', 'amsterdam', 'china']
print(places)

print("\nThe first three items in the list are:")
print(places[0:3])

print("\nThree items from the middle of the list are:")
print(places[1:4])

print("\nThe last three items in the list are:")
print(places[2:5])




print(sorted(places))
print(places)
# (sorted() temporary sort for alphabetical order

places.reverse()
print(places)
# .reverse() literally reveses the order of the list.

places.sort(reverse = True)
print(places)
# reversing it back to original order

places.sort()
print(places)
# list manipulated back in alphabetical order

places.reverse()
print(places)


