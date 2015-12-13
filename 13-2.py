import itertools

connections = list()
with open('13.txt','r') as f:
	connections = f.read().split('\n')

people = list()
for path in connections:
	nodeList = path.split(" ")
	if not nodeList[0] in people:
		people.append(nodeList[0])
	if not nodeList[10][:-1] in people:
		people.append(nodeList[10][:-1])
people.append("Me")

possible_configurations = list(itertools.permutations(people,len(people)))

def happinessScore(person, friend):
	score = 0
	if person == "Me" or friend == "Me":
		return 0
	for pathdef in connections:
		if pathdef.split(" ")[0] == person and pathdef.split(" ")[10][:-1] == friend:
			score = int(pathdef.split(" ")[3])
			if pathdef.split(" ")[2] == "lose":
				score *= -1
			return score

best_happiness = None
print "Checking through " + str(len(possible_configurations)) + " possible configurations"
index = 0
for arrangement in possible_configurations:
	score = 0
	for x in range(len(arrangement)):
		if x != len(arrangement) - 1:
			score += happinessScore(arrangement[x], arrangement[x+1])
			score += happinessScore(arrangement[x+1], arrangement[x])
		else:
			score += happinessScore(arrangement[x], arrangement[0])
			score += happinessScore(arrangement[0], arrangement[x])
	if best_happiness is None or score > best_happiness:
		best_happiness = score
	index += 1
	if index % 5000 == 0:
		print str(100*float(index)/len(possible_configurations)).split(".")[0] + "% complete"

print "Happiness of optimal arrangement: " + str(best_happiness)
