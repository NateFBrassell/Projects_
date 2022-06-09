motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
# append() adds elements to the end of a list

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# insert()allows you to add an element to your list at any position you want.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
# del allows you to remove an item from the list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# pop() add which space you want to pull from.. popped_motorcycle means you can show value of popped motorcycle from the list but also still have access to it.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + ".")

# when you want to delete an item from a list and not use that item in any was, use the del statment; if you want to use an item as you remove it, us the pop() method.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)


too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

print("The first three items in the list are:")
print(motorcycles[0:3])
print("\nThree items in the middle of the list are:")
print(motorcycles[1:3])


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
# example of an index code error. Rememeber list count starts at 0.
# page 50 3-10 needs done.



