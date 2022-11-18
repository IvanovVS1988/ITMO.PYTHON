# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

d1 = 3*float(input("Input distance d1 in yards: "))
d2 = float(input("Input distance d2 in feet: "))
h = 3*float(input("Input h in yards: "))
v_sand = 5280*float(input("Input speed v_sand in m/h: "))/3600
n = float(input("Input n cofficient: "))
theta1 = float(input("Input angel in deegres: "))/57.295782

L1 = d1/math.cos(theta1)
x = L1*math.sin(theta1)

if x > h:
    print("Input angel is to big")
else:
    L2 = math.sqrt((h-x)**2+d2**2)
    time = L1/v_sand + L2/(v_sand/n)
    print("Спасатель достигнет утопающего через: " + str(time) + " секунды")
    