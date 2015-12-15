stats_raw = list()
with open('14.txt','r') as f:
	stats_raw = f.read().split('\n')

"""
Stats saved in the format "NAME":(SPEED,DURATION,CURR_DURATION,REST_TIME,CURR_REST,DIST)
"""
class Raindeer:
	def __init__(self, speed, duration, rest_time,name):
		self.name = name
		self.speed = speed
		self.duration = duration
		self.rest_time = rest_time
		self.curr_duration = 0
		self.curr_rest = 0
		self.dist = 0
		self.points = 0

raindeer = list()
for deer in stats_raw:
	info = deer.split()
	raindeer.append(Raindeer(int(info[3]),int(info[6]),int(info[-2]), info[0]))

def get_farthest_raindeers(raindeer_list):
	farthest_dist = -1
	farthest = list()
	for deer in raindeer_list:
		if deer.dist == farthest_dist:
			farthest.append(deer)
		elif deer.dist > farthest_dist:
			farthest = list()
			farthest.append(deer)
			farthest_dist = deer.dist
	return farthest

seconds_to_simulate = 2503
for x in range(seconds_to_simulate):
	for deer in raindeer:
		#Running
		if deer.curr_duration < deer.duration:
			deer.dist += deer.speed
			deer.curr_duration += 1
		#Resting
		elif deer.curr_rest < deer.rest_time - 1:
			deer.curr_rest += 1
		elif deer.curr_rest >= deer.rest_time - 1:
			deer.curr_rest = 0
			deer.curr_duration = 0
	for winner in get_farthest_raindeers(raindeer):
		winner.points += 1
		
best = None
for deer in raindeer:
	if best is None or deer.points > best.points:
		best = deer
print "...And the winner is... " + best.name + " with " +str(best.points) + " points!"