#!/usr/bin/python3

import sys


n = int(input().strip())

for i in range(1, 11):
    product = n*i
    print (n, "x", i, "=", product)
