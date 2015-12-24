import itertools
from operator import mul


weights = list()
with open('24.txt','r') as f:
	weights = f.read().split('\n')

weights = [int(i) for i in weights]

def find_smallest_group(num_groups):
	group_sum = sum(weights) / num_groups
	found_groups = list()
	for i in range(len(weights)):
		possible_combos = list(itertools.combinations(weights,i))
		for combo in possible_combos:
			if sum(combo) == group_sum:
				found_groups.append(combo)
		if len(found_groups) > 0:
			min_QE = 2**100
			min_QE_index = 0
			for i in range(len(found_groups)):
				QE = reduce(mul, found_groups[i], 1)
				if QE < min_QE:
					min_QE = QE
					min_QE_index = i
			print "The minimum Quantum Entanglement of " + str(num_groups) + " groups is " + str(min_QE)
			return 

find_smallest_group(3)
find_smallest_group(4)