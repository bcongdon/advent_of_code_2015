path = ""

with open("1.txt","r") as f:
	path += f.read()

floor = 0
pos = 0
basement = False
for step in path:
	pos += 1
	if step == '(':
		floor += 1
	if step == ')':
		floor -= 1
	if floor < 0 and not basement:
		print pos
		basement = True
print floor