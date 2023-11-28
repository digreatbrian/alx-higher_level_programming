#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
        if not chr(char) in ['q', 'e']:
        	print(chr(char), end='')
        	