
instructions = list()
with open("6.txt", "r") as f:
	instructions = f.read().split('\n')

temp = list()
for step in instructions:
	if step.startswith('turn off'):
		temp.append('turnoff' + step.split('turn off')[1])
	elif step.startswith('turn on'):
		temp.append('turnon' + step.split('turn on')[1])
	else:
		temp.append(step)
instructions = temp

lights = dict()
for x in range(1000):
	for y in range(1000):
		lights[(x,y)] = 0

def toggle(x1,y1,x2,y2):
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			lights[(x,y)] += 2

def turnoff(x1,y1,x2,y2):
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			lights[(x,y)] -= 1
			if lights[(x,y)] < 0:
				lights[(x,y)] = 0

def turnon(x1,y1,x2,y2):
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			lights[(x,y)] += 1

for step in instructions:
	parts = step.split(" ")
	x1 = int(parts[1].split(',')[0])
	y1 = int(parts[1].split(',')[1])
	x2 = int(parts[3].split(',')[0])
	y2 = int(parts[3].split(',')[1])
	if parts[0] == "turnoff":
		turnoff(x1,y1,x2,y2)
	elif parts[0] == "turnon":
		turnon(x1,y1,x2,y2)
	elif parts[0] == "toggle":
		toggle(x1,y1,x2,y2)
print 'Total brightness after executing instructions: ' + str(sum(lights.values()))