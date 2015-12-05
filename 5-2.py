
children = list()
with open("5.txt", "r") as f:
	children = f.read().split('\n')

def num_occurences(whole, part):
	if whole == "":
		return 0
	if whole.startswith(part):
		return 1 + num_occurences(whole[2:],part)
	else:
		return num_occurences(whole[1:],part)

def is_good(child):
	found = False
	for i in range(0,len(child) - 2):
		if child[i] == child[i+2]:
			found = True
			break
	if not found:
		return False
	found = False
	for i in range(0,len(children)):
		if len(child[i:i+2]) < 2:
			break
		if num_occurences(child,child[i:i+2]) > 1:
			found = True
			break
	return found
	
print [is_good(i) for i in children].count(True)