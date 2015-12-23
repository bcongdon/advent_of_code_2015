def simulate(actions):
    boss_hp = 58
    boss_damage = 9
    mana = 500
    spent = 0
    shield = 0
    poison = 0
    recharge = 0
    hp = 50
    turn_c = 0
    my_turn = 1
    spell_costs = {'M':53, 'D':73, 'S':113, 'P':173, 'R':229}

    while True:
        if len(actions)-1 < turn_c:
            return 0
        if poison:
            poison = max(poison - 1, 0)
            boss_hp -= 3
        if shield:
            shield = max(shield - 1, 0)
            armor = 7
        else:
            armor = 0
        if recharge:
            recharge = max(recharge - 1, 0)
            mana += 101
        action = actions[turn_c]    
        if my_turn == 1:
            mana -= spell_costs[action]
            spent += spell_costs[action]
            if action == "M":
                boss_hp -= 4
            elif action == 'D':
                boss_hp -= 2
                hp += 2
            elif action == 'S':
                if shield:
                    return 0
                shield = 6
            elif action == 'P':
                if poison:
                    return 0
                poison = 6
            elif action == 'R':
                if recharge:
                    return 0
                recharge = 5
            if mana < 0:
                return 0
        if boss_hp <= 0:
            return spent, actions[:turn_c+1]
        if my_turn == -1:
            hp -= max(boss_damage - armor, 1)
            if hp <= 0:
                return 0
        if my_turn == 1:
            turn_c += 1
        my_turn = -my_turn

def iterate(index):
    new_pos = 'MDSPR'.index(actions[index])
    actions[index] = 'DSPRM'[new_pos]
    if actions[index] == 'M':
        if index+1 <= len(actions):
            iterate(index+1)

actions = ['M'] * 20
min_spent = 2**100
min_combo = ''
for i in range(1000000):
    result = simulate(actions)
    if isinstance(result,tuple):
        min_spent = min(result[0], min_spent)
        min_combo = result[1]
    iterate(0)    
print "Minimum Mana spent: " + str(min_spent) + " With action combo: \"" + str(''.join(min_combo)) + "\""