import math
houses = list()

def sum_factors(num):
	count = 0
	small_divisors = list()
	for x in range(1,int(math.sqrt(num)) + 1):
		if num % x == 0:
			small_divisors.append(x)
	large_divisors = [num / div for div in small_divisors if num != div * div]
	return sum(large_divisors + small_divisors)


target_sum = 29000000

for x in range(1,29000000):
	if x % 1000 == 0:
		print x, sum_factors(x)
	if sum_factors(x) * 10 >= target_sum:
		print "There are " + str(sum_factors(x)) + " presents at house #" + str(x)
		break