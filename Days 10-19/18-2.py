initial_conditions = list()
with open('18.txt','r') as f:
	initial_conditions = f.read().split('\n')

width = len(initial_conditions)
height = len(initial_conditions[0])
lights = [[False for x in xrange(width)] for y in xrange(height)]

for x in range(width):
	for y in range(height):
		if initial_conditions[x][y] == '#':
			lights[x][y] = True
		if initial_conditions[x][y] == '.':
			lights[x][y] = False

#Lights stuck on
lights[0][0] = True
lights[width - 1][0] = True
lights[0][height - 1] = True
lights[width - 1][height - 1] = True

def num_neighbors(x,y):
	count = 0
	#Up/Down/Left/Right
	if x > 0 and lights[x-1][y]:
		count += 1
	if x < width - 1 and lights[x+1][y]:
		count += 1
	if y > 0 and lights[x][y-1]:
		count += 1
	if y < height - 1 and lights[x][y+1]:
		count += 1
	#Diagonals
	if x < width - 1 and y < height - 1 and lights[x+1][y+1]:
		count += 1
	if x < width - 1 and y > 0 and lights[x+1][y-1]:
		count += 1
	if x > 0 and y > 0 and lights[x-1][y-1]:
		count += 1
	if x > 0 and y < height - 1 and lights[x-1][y+1]:
		count += 1
	return count
num_steps = 100
for step in range(num_steps):
	temp_array = [[False for x in xrange(width)] for y in xrange(height)]
	for x in range(width):
		for y in range(height):
			if lights[x][y]:
				if num_neighbors(x,y) == 2 or num_neighbors(x,y) == 3:
					temp_array[x][y] = True
				else:
					temp_array[x][y] = False
			else:
				if num_neighbors(x,y) == 3:
					temp_array[x][y] = True
				else:
					temp_array[x][y] = False
	#Force lights on
	temp_array[0][0] = True
	temp_array[width - 1][0] = True
	temp_array[0][height - 1] = True
	temp_array[width - 1][height - 1] = True
	lights = temp_array

lights_on = 0
for x in range(width):
	for y in range(height):
		if(lights[x][y]):
			lights_on += 1
print "After " + str(num_steps) + " seconds, " + str(lights_on) + " lights are on."