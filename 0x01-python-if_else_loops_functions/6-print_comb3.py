#!/usr/bin/python3
for a in range(10):
	for b in range(10):
		if (a < b):
			if not (a == 8 and b == 9):
				print("{:02d}".format(int("%s%s" % (a, b))), end = ', ')
			else:
				print("{:02d}".format(int("%s%s" % (a, b))))