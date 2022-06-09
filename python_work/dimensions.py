dimensions = (200, 50)
#dimensions[0] =250 this is beneficial because we want python to raise an error when a line of code tries to change the dimensions of the object.
print(dimensions[0])
print(dimensions[1])


dimensions = (200, 50)
for dimension in dimensions:
    print(dimensions)
    

dimensions = (200, 50)
print("Original dimensins:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    

