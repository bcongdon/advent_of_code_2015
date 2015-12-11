def isPassword(string):
	#No Illegal Chars
	if ['i','o','l'] in list(string):
		return False

	#Has Increasing
	found_inc = False
	for x in range(len(string)-2):
		if ord(string[x]) + 1 == ord(string[x+1]) and ord(string[x+1]) + 1 == ord(string[x+2]):
			found_inc = True
			break
	if not found_inc:
		return False

	#Two non-overlapping pairs
	if repeating_pairs(string) < 2:
		return False
	return True

def repeating_pairs(string):
	if len(string) <= 1:
		return 0
	if string[0] == string[1]:
		return 1 + repeating_pairs(string[2:])
	else:
		return repeating_pairs(string[1:])

def nextPassword(string):
	if string[-1] == 'z':
		return nextPassword(string[:-1]) + 'a'
	string = string[:-1] + unichr(ord(string[-1]) + 1)
	return string

puzzle_input = nextPassword('hepxxyzz')
while not isPassword(puzzle_input):
	puzzle_input = nextPassword(puzzle_input)
print puzzle_input