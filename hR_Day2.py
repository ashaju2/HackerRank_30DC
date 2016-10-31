#!/usr/bin/python3

import sys

mealCost = float(input())

tipPercent = int(input())

taxPercent = int(input())
t_Cost = round(((tipPercent/100) * mealCost) + mealCost + ((taxPercent/100) * mealCost))
print("The total meal cost is " + str(t_Cost) +  " dollars.")