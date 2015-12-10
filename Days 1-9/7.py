
instructions = list()
"""
Use either 7.txt or 7-2.txt for parts 1 and 2 of today's problem
"""
with open('7-2.txt','r') as f:
	instructions = f.read().split('\n')

instructions = [i.split("->") for i in instructions]
temp = list()
for step in instructions:
	temp2 = list()
	for part in step:
		temp2.append(part.split())
	temp.append(temp2)
instructions = temp

values = dict()
def find_value(a):
	#Base case (a is a defined quantity)
	if a.isdigit():
		return int(a)
	#The value of a is already known (memorization)
	if a in values.keys():
		return values[a]

	#Find the instruction that leads to the output 'a'
	determining_step = ""
	for step in instructions:
		if step[1][0] == a:
			determining_step = step
	#Fail if the step isn't found (state of 'a' is indeterminable)
	if determining_step == "":
		raise UserWarning

	#Catch Values
	print determining_step
	if len(determining_step[0]) == 1:
		values[a] = find_value(determining_step[0][0])
		return values[a]
	#Catch "NOT"
	if determining_step[0][0] == "NOT":
		values[a] = (~find_value(determining_step[0][1]) & 0xffff)
		return values[a]
	#Recursively find values of the two inputs
	in1 = int(find_value(determining_step[0][0]))
	in2 = int(find_value(determining_step[0][2]))
	#Do the operation requested
	if determining_step[0][1] == "OR":
		values[a] = in1 | in2
	if determining_step[0][1] == "AND":
		values[a] = in1 & in2
	if determining_step[0][1] == "RSHIFT":
		values[a] = in1 >> in2
	if determining_step[0][1] == "LSHIFT":
		values[a] = in1 << in2
	return values[a]

print find_value("a")
