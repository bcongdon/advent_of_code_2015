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
special = ['cats','trees','pomeranians','goldfish']
for aunt in raw:
	parsed = aunt.split(' ')
	count = 0
	for x in range(3):
		value = parsed[2*x+3]
		key = parsed[2*x+2][:-1]
		if len(value) > 1:
			value = value[:-1]
		value = int(value)
		if not key in special:
			if key in known_stats.keys() and value == known_stats[key]:
				count += 1
		elif key in special[:2] and value > known_stats[key]:
			count += 1
		elif key in special[2:] and value < known_stats[key]:
			count += 1
	if count == 3:
		correct_aunt = int(parsed[1][:-1])
print "The correct Aunt Sue is Sue #" + str(correct_aunt)