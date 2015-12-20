import math
houses = list()

def sum_factors(num):
	count = 0
	small_divisors = list()
	for x in range(1,int(math.sqrt(num)) + 1):
		if num % x == 0:
			small_divisors.append(x)
	large_divisors = [num / div for div in small_divisors if num != div * div]
	return (large_divisors + small_divisors)


target_sum = 29000000

for x in range(1,29000000):
	count = sum(div for div in sum_factors(x) if x / div <= 50) * 11
	if x % 1000 == 0:
		print x, count
	if count >= target_sum:
		print "There are " + str(count) + " presents at house #" + str(x)
		break