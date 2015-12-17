import itertools
sizes = list()

with open('17.txt','r') as f:
	sizes = [int(i) for i in f.read().split('\n')]

desired_total = 150
valid_found = 0
valid_minimum_found = 0
minimum_length = None
for x in range(len(sizes)):
	select = x + 1
	for comb in list(itertools.combinations(sizes,select)):
		if sum(comb) == desired_total:
			if minimum_length is None or len(comb) < minimum_length:
				valid_minimum_found = 1
				minimum_length = len(comb)
			elif len(comb) == minimum_length:
				valid_minimum_found += 1
			valid_found += 1

print "Number of valid combinations found: " + str(valid_found)
print "Minimum Length: " + str(minimum_length) + ", with " + str(valid_minimum_found) + " combinations at that length."