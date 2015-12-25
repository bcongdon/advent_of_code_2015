def next_in_sequence(curr):
	return (curr * 252533) % 33554393

def index_at_coord(x,y):
	final_index = 1
	for i in range(1,x):
		final_index += i + 1
	inc = x
	for j in range(1,y):
		final_index += inc
		inc += 1
	return final_index

def find_value_at(col,row):
	index_needed = index_at_coord(col,row)

	val = 20151125
	index_needed -= 1
	for i in range(index_needed):
		val = next_in_sequence(val)
	print "The value at column (" + str(col) + ") and row (" + str(row) + ") is " +str(val) + "."
	print "This value is at the " + str(index_needed) + "th index of the sequence."

find_value_at(3083,2978)