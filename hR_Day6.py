#!/usr/bin/python3

import sys

n = int(input().strip())

for i in range(0,n):
	string = input()
	letters = list(string)
	j = letters[0::2]
	k = letters[1::2]
	print(''.join(j), ''.join(k))
		

