presents = list()
with open("2.txt","r") as f:
	presents = f.read().split('\n')

formatted = list()
for present in presents:
	formatted.append([int(i) for i in present.split('x')])

def get_SA(dimens):
	l = dimens[0]
	w = dimens[1]
	h = dimens[2]
	sides = [2*l*w, 2*w*h, 2*h*l]
	reg = sum(sides)
	slack = min(sides)/2
	return reg + slack

def get_ribbon(dimens):
	smallest_perim = 2*(sum(dimens) - max(dimens))
	cubic = reduce(lambda x, y: x * y, dimens, 1)
	return cubic + smallest_perim


print "Sqft. Paper Needed: " + str(sum([get_SA(i) for i in formatted]))
print "Ft. Ribbon Needed: " + str(sum([get_ribbon(i) for i in formatted]))