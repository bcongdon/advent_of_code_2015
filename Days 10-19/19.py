puzzle_challange = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

definitions_raw = list()
with open('19.txt','r') as f:
	definitions_raw = f.read().split('\n')

definitions = list()
for rep in definitions_raw:
	definitions.append(rep.split(" => "))

molecules = set()
for before, after in definitions:
	loc = -1
	i = 0
	indexes = []
	while True:
		i += 1
		loc = puzzle_challange.find(before, loc + 1)
		if loc != -1:
			indexes.append(loc)
		else:
			break
	for current in indexes:
		molecules.add(puzzle_challange[0:current] + after + puzzle_challange[current+len(before):])
print len(molecules)