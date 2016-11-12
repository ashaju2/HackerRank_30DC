#!/usr/bin/python3

import sys

def factorial(n):
    if n == 0:
        return(1)
    if n > 0 or n < 0:
        return (abs(n) * factorial(abs(n)-1))
    
    
print(factorial(int(input())))
