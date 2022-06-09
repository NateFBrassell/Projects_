# A simple dictionary.

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# Accessing Values in a Dictionary.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])


alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary.
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary.
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3
	
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# A dictionary in a dictionary.
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
		
	}
	
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
print("\tFull name: " + full_name.title())
print("\tLocation: " + location.title())

