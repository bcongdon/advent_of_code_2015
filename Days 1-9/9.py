import itertools

pathdefs = list()
with open('9.txt','r') as f:
	pathdefs = f.read().split('\n')

nodes = list()
for path in pathdefs:
	nodeList = path.split(" ")
	if not nodeList[0] in nodes:
		nodes.append(nodeList[0])
	if not nodeList[2] in nodes:
		nodes.append(nodeList[2])

possible_paths = list(itertools.permutations(nodes,len(nodes)))

def link_length(a,b):
	for pathdef in pathdefs:
		if pathdef.split(" ")[0] == a and pathdef.split(" ")[2] == b:
			return int(pathdef.split(" ")[4])
		if pathdef.split(" ")[2] == a and pathdef.split(" ")[0] == b:
			return int(pathdef.split(" ")[4])

smallest_path = 10**10
largest_path = 0
for path in possible_paths:
	path_length = 0
	valid = True
	for x in range(0,len(path) - 1):
		if link_length(path[x],path[x+1]) is not None: 
			path_length += link_length(path[x],path[x+1])
		else:
			valid = False
	if valid and path_length < smallest_path:
		smallest_path = path_length
	if valid and path_length > largest_path:
		largest_path = path_length
print "Length of smallest path: " + str(smallest_path)
print "Length of largest path: " + str(largest_path)
