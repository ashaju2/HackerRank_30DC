#!/usr/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
newArr = [arr[(len(arr)-1)-i] for i in range(len(arr))]

print(*newArr)
