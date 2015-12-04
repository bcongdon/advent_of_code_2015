directions = list()
visited = dict()
with open("3.txt","r") as f:
	directions = f.read()

visited[(0,0)] = True
santaX = 0
santaY = 0
robotX = 0
robotY = 0
santasTurn = False
for step in directions:
	if step == ">":
		if santasTurn:
			santaX += 1
		else:
			robotX += 1
	if step == "<":
		if santasTurn:
			santaX -= 1
		else:
			robotX -= 1
	if step == "^":
		if santasTurn:
			santaY += 1
		else:
			robotY += 1
	if step == "v":
		if santasTurn:
			santaY -= 1
		else:
			robotY -= 1
	visited[(santaX,santaY)] = True
	visited[(robotX,robotY)] = True
	santasTurn = not santasTurn
print len(visited.keys())