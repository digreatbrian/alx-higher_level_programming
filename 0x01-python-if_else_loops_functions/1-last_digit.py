#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = ''
if number > 5:
	s = 'and is greater than 5'
elif number == 0:
	s = 'and is 0'
else:
	s = 'and is less than 6 and not 0'
	
print("Last digit of %d is %s %s" % (number, str(number)[-1], s))
