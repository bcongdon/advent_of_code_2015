import sys
sys.setrecursionlimit(5000)

instructions = list()
with open('23.txt','r') as f:
	instructions = f.read().split('\n')

registers = {'a':0,'b':0}
def do_step(num):
	print registers,
	if num >= len(instructions):
		return
	step = instructions[num].split(' ')
	opcode = step[0]
	print step
	if opcode == 'hlf':
		registers[step[1]] /= 2
		do_step(num+1)
	elif opcode == 'tpl':
		registers[step[1]] *= 3
		do_step(num+1)
	elif opcode == 'inc':
		registers[step[1]] += 1
		do_step(num+1)
	elif opcode == 'jmp':
		if step[1][0] == '+':
			do_step(num + int(step[1][1:]))
		else:
			do_step(num - int(step[1][1:]))
	elif opcode == 'jie':
		if registers[step[1][0]] % 2 == 0:
			if step[2][0] == '+':
				do_step(num + int(step[2][1:]))
			else:
				do_step(num - int(step[2][1:]))
		else:
			do_step(num+1)
	elif opcode == 'jio':
		if registers[step[1][0]] == 1:
			if step[2][0] == '+':
				do_step(num + int(step[2][1:]))
			else:
				do_step(num - int(step[2][1:]))
		else:
			do_step(num+1)

do_step(0)
reg_b_when_a_0 = registers['b']
registers = {'a':1,'b':0}
print '-------------------'
do_step(0)
print "Starting with registers (a:0, b:0) the value of \"b\" after operation is " + str(reg_b_when_a_0)
print "Starting with registers (a:1, b:0) the value of \"b\" after operation is " + str(registers['b'])
