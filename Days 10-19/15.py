input_txt = list()
with open('15.txt','r') as f:
	input_txt = f.read().split('\n')

ingredients = list()
for line in input_txt:
	data = line.split(" ")
	"""
	NAME, CAPACITY, DURABILITY, FLAVOR, TEXTURE, CALORIES
	"""
	ingredients.append((data[0][:-1],
						int(data[2][:-1]),
						int(data[4][:-1]),
						int(data[6][:-1]),
						int(data[8][:-1]),
						int(data[10])))

def cookie_score(quantities):
	scores = list()
	for z in range(1,5):
		temp = 0
		for x in range(len(quantities)):
			temp += quantities[x] * ingredients[x][z]
		if temp < 0:
			return 0
		else:
			scores.append(temp)
	score_total = 1
	for s in scores:
		score_total *= s
	return score_total

# a,b,c,d represent teaspoons of the different ingredients
max_score = 0
ingredients_at_max = ()
for a in range(0,101):
	for b in range(101 - a):
		for c in range(101 - a - b):
			d = 100 - a - b - c
			score = cookie_score([a,b,c,d])
			if score > max_score:
				max_score = score
				ingredients_at_max = (a,b,c,d)
print "Best possible cookie has " + str(max_score) + " points."
print ("Recipe: " + str(ingredients_at_max[0]) + "tsp Sprinkles, " + str(ingredients_at_max[1]) + "tsp Butterscotch, " +
	str(ingredients_at_max[2]) + "tsp Chocolate, " + str(ingredients_at_max[3]) + "tsp Candy.")

