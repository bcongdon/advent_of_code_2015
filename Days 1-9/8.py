strings = list

with open('8.txt','r') as f:
	strings = f.read().split()

def num_string_total(string):
	return len(eval(string))

def num_literals(string):
	return len(string) 

def len_encode(string):
	return 2 + string.count('"') + string.count("\\")

print "Part 1: " + str(sum([num_literals(i) for i in strings]) - sum([num_string_total(i) for i in strings]))
print "Part 2: " + str(sum([len_encode(i) for i in strings]))