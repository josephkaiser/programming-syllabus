'''
aliens.py
PCC
Ch 6
practice with dictionaries
'''

alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'fast','points': 5, 'color': 'green'}
print(f"alien 0: {alien_0}")
print("Original x-position: " + str(alien_0['x_pos']))

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
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

print("New x-position: " + str(alien_0['x_pos']))

# Remove points
print('removing points key from alien_0 dictionary along with its value')
del alien_0['points']
print(f"alien 0: {alien_0}")


# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")
#
# alien_0['color'] = 'yellow'
# print("The alien is " + alien_0['color'] + ".")

# alien_0 = {} # Initialize empty dictionary
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'blue', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = {'alien_0': alien_0, 'alien_1': alien_1, 'alien_2': alien_2}
#
# print(alien_0['color'])
# print(alien_0['points'])
#
# print(aliens['alien_1']['color'])
# print(aliens['alien_1']['points'])
#
# new_points = alien_1['points']
#
# print(f"You just earned {new_points} points!")
#
# alien_0['x_pos'] = 0
# alien_0['y_pos'] = 25
# print(alien_0)
