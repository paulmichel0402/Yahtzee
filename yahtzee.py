import random

die1 = 1
die2 = 2
die3 = 3
die4 = 4
die5 = 5
comp = False
ctr = 1
sums = 0

def roll():
	global die1 #= random.randint(1,6)
	global die2 #= random.randint(1,6)
	global die3 #= random.randint(1,6)
	global die4 #= random.randint(1,6)
	global die5 #= random.randint(1,6)
	global ctr
	global sums

	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	die3 = random.randint(1,6)
	die4 = random.randint(1,6)
	die5 = random.randint(1,6)
	ctr = ctr + 1
	return


def compare(d1,d2,d3,d4,d5):
	if d1 != d2:
		return False
	elif d1 != d3:
		return False
	elif d1 != d4:
		return False
	elif d1 != d5:
		return False
	elif d2 != d3:
		return False
	elif d2 != d4:
		return False
	elif d2 != d5:
		return False
	elif d3 != d4:
		return False
	elif d3 != d5:
		return False
	elif d4 != d5:
		return False
	else:
		return True


for i in range(0,1000):
	ctr = 1
	roll()
	comp = compare(die1,die2,die3,die4,die5)
	while comp != True:
		roll()
		comp = compare(die1,die2,die3,die4,die5)
	sums = sums + ctr

print "Average number of rolls before Yahtzee was: " + str(sums/1000)


