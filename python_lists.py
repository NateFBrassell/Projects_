cars = ['chevy', 'chrystler', 'saturn', 'dodge', 'ford']
print(cars)
print(cars[0])
print(cars[2].title())
print(cars[-1])

message = "My first car was a " + cars[-2].title() + "."
print(message)

cars[3] = 'tesla'
print(cars)

cars.append('toyota')
print(cars)

teams = []

teams.append('cincinatti bengals')
teams.append('baltimore ravens')
teams.append('san diego chargers')
teams.append('seattle seahawks')
teams.append('atlanta falcons')
print(teams)

teams.insert(1, 'cleveland browns')
print(teams)

del teams[3]
print(teams)

popped_teams = teams.pop()
print(teams)
print(popped_teams)

laptops = ['acer', 'asus', 'dell', 'lenovo', 'macbook']
print(laptops)

too_expensive = 'macbook'
laptops.remove(too_expensive)
print(laptops)
print("\nA " + too_expensive.title() + " is too expensive for me.")

laptops.sort()
print(laptops)

laptops.sort(reverse=True)
print(laptops)

laptops = ['dell', 'macbook', 'acer', 'lenovo', 'asus']
print("Here is the orginal list:")
print(laptops)

print("\nHere is the sorted list:")
print(sorted(laptops))

print("\nHere is the orginal list again:")
print(laptops)

print("\nHere is the list of laptops in reverse sort.")
laptops.reverse()
print(laptops)

print("\nHere is the number of items in the list.")
print(len(laptops))


