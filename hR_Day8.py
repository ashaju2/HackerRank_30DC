#!/usr/bin/python3

import sys

n = int(input())
telephone = {}
for j in range(n):
    x = input().split(" ")
    telephone[x[0]] = x[1]
    
names = []

for k in range(n):
    names.append(input()) 
for name in names:
    if name in telephone:
        print(name + "=" + telephone[name])
    else:
        print("Not found")
    
    

