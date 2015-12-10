import md5
m = md5.new()

def gen_zero_string(x):
	string = ""
	for i in range(x):
		string += '0'
	return string

numZeros = 6
checkNum = 1
challange = 'bgvyzdsv'

checkString = gen_zero_string(numZeros)
while True:
	m = md5.new()
	m.update(challange + str(checkNum))
	adventHash = m.hexdigest()
	checkNum += 1
	if adventHash.startswith(checkString):
		print adventHash, checkNum - 1
		break