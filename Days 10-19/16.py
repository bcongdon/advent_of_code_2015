raw = list()
with open('16.txt','r') as f:
	raw = f.read().split('\n')

known_stats = {
	"children":3,
	"cats":7,
	"samoyeds":2,
	"pomeranians":3,
	"akitas":0,
	"vizslas":0,
	"goldfish":5,
	"trees":3,
	"cars":2,
	"perfumes":1
}
correct_aunt = 0
for aunt in raw:
	parsed = aunt.split(' ')
	count = 0
	if parsed[2][:-1] in known_stats.keys() and int(parsed[3][:-1]) == known_stats[parsed[2][:-1]]:
		count += 1
	if parsed[4][:-1] in known_stats.keys() and int(parsed[5][:-1]) == known_stats[parsed[4][:-1]]:
		count += 1
	if parsed[6][:-1] in known_stats.keys() and int(parsed[7]) == known_stats[parsed[6][:-1]]:
		count += 1
	if count == 3:
		correct_aunt = int(parsed[1][:-1])
print "The correct Aunt Sue is Sue #" + str(correct_aunt)