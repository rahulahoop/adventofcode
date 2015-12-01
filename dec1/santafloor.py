import sys

filename = "./input.txt"
m_goUp = "("
m_goDown = ")"
finalFloor = 0

def parse(c):
	if c == m_goUp:
		global finalFloor
		finalFloor += 1
	elif c == m_goDown:
		global finalFloor
		finalFloor -= 1

with open(filename) as f:
	while True:
		c = f.read(1)
		if c:
			parse(c)
		else:
			print finalFloor
			break
		print "read a char: ", c
