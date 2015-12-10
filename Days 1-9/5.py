
children = list()
with open("5.txt", "r") as f:
	children = f.read().split('\n')

bad_strings = ['ab','cd','pq','xy']
vowels = 'aeiou'
def is_good(child):
	count = 0
	for i in child:
		if i in vowels:
			count += 1
	if count < 3:
		return False
	found = False
	for i in range(0,len(child) - 1):
		if child[i] == child[i+1]:
			found = True
			break

	if not found:
		return False

	for s in bad_strings:
		if s in child:
			return False
	return True
print [is_good(i) for i in children].count(True)
