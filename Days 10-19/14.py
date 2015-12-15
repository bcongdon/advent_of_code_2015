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

raindeer = list()
for deer in stats_raw:
	info = deer.split()
	raindeer.append(Raindeer(int(info[3]),int(info[6]),int(info[-2]), info[0]))

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
		
farthest = None
for deer in raindeer:
	if farthest is None or deer.dist > farthest.dist:
		farthest = deer
print "...And the winner is... " + farthest.name + ", having travelled " + str(farthest.dist) + "km!"