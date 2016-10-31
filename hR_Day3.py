#!/usr/bin/python3

import sys

N = int(input().strip())
x = 'Weird'
if ((N%2) == 1):
    print(x)
else:
    if ((2 <= N <= 5) or (N > 20)):
        x = 'Not Weird'
        print(x)
    else:
        print(x)