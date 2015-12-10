def process_string(string):
	count = 0
	char = ''
	output = ''
	for x in range(len(string)):
		if char == '':
			char = string[x]
		if char == string[x]:
			count += 1
		elif count > 0:
			output += str(count) + char
			char = string[x]
			count = 1
	output += str(count) + char
	return output

string = '1113122113'
for x in range(40):
	string = process_string(string)
print "40 iterations: " + str(len(string))

string = '1113122113'
for x in range(50):
	string = process_string(string)
print "50 iterations: " + str(len(string))
