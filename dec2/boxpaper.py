import re

filename = "input.txt"
totalFeet = 0
totalRibbon = 0

def smallestSides(l,w,h):
	dim = [l,w,h]
	m = max(dim)
	dim.remove(m)
	return dim

def ribbon(l,w,h):
	presentDim = smallestSides(l,w,h)
	present = presentDim[0]*2 + presentDim[1]*2
	bow = l * w * h
	return present + bow

def SA(l,w,h):
	return 2*l*w + 2*w*h + 2*h*l

def slack(l,w,h):
	dim = smallestSides(l,w,h)
	s = dim[0] * dim[1]
	return s

def parse(dimGroup):
	length = int(dimGroup.group(1))
	width = int(dimGroup.group(2))
	height = int(dimGroup.group(3))

	surfaceArea = 0
	slck = 0

	surfaceArea = SA(length, width, height)
	
	global totalFeet, totalRibbon
	totalFeet = totalFeet + surfaceArea + slack(length, width, height)
	totalRibbon = totalRibbon + ribbon(length, width, height)

with open(filename) as f:
	for line in f:
		curLine = re.search(r'(\d*)x(\d*)x(\d*)', line)
		parse(curLine)
	print "Presents: " + str(totalFeet)
	print "Ribbon: " + str(totalRibbon)
