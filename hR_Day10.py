#!/usr/bin/python3

import sys
import math

x = []
newList = []

count = 1
n = int(input().strip())


if n == 0:
    x.append(n)

    
while n > 0:
    x.append(n%2)
    n = math.floor(n/2)

    
x.reverse()

for num in range(len(x) - 1):
    if x[num] == x[num + 1]:
        count = count + 1
    else:
        newList.append(count)
        count = 0
        
print(max(newList))
    
