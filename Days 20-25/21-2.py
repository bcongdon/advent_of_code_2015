import itertools

weapons_cost = [8,10,25,40,74]
weapons_damage = [4,5,6,7,8]

armor_cost = [0,13,31,53,75,102]
armor_rating = [0,1,2,3,4,5]

ring_cost = [25,50,100,20,40,80]
ring_damage = [1,2,3,0,0,0]
ring_rating = [0,0,0,1,2,3]


def would_win(damage, armor):
	my_hp = 100
	boss_hp = 104
	boss_damage = 8
	boss_armor = 1
	while my_hp > 0 and boss_hp > 0:
		boss_hp -= max([(damage - boss_armor),1])
		if boss_hp <= 0:
			return True
		my_hp -= max([boss_damage - armor, 1])
		if my_hp <= 0:
			return False

most = 0
#Weapons
for w in range(len(weapons_damage)):
	#Armor
	for a in range(len(armor_cost)):
		#Rings
		for r in range(3):
			rings_combos = list(itertools.combinations([x for x  in range(len(ring_cost))],r))
			for ring_combo in rings_combos:
				damage = weapons_damage[w] + sum([ring_damage[i] for i in ring_combo])
				rating = armor_rating[a] + sum([ring_rating[i] for i in ring_combo])
				cost = weapons_cost[w] + armor_cost[a] + sum([ring_cost[i] for i in ring_combo])
				if not would_win(damage, rating):
					if cost > most:
						most = cost
print most