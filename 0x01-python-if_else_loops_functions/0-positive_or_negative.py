#!/usr/bin/python3
import random
number = random.randint(-10, 10)
state = ''
if number > 0:
	state = 'is positive'
elif number == 0:
	state = 'is zero'
else:
	state = 'is negative'
print("%d %s" % (number, state))
