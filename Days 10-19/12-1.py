import json

json_in = list()
with open('12.json','r') as f:
	json_in = json.loads(f.read())

def traverse_tree(head):
	if isinstance(head,int):
		return head
	total = 0
	if isinstance(head,list):
		for elem in head:
			total += traverse_tree(elem)
	elif isinstance(head,dict):
		for elem in head.values():
			total += traverse_tree(elem)
	return total
	

print traverse_tree(json_in)