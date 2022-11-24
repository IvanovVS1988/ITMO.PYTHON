# -*- coding: utf-8 -*-

import math

YARDS_PER_FOOT = 3
FETT_PER_MILE = 5280
SECONDS_PER_HOUR = 3600
DEGREES_PER_RADIAN = 57.295782

d1 = YARDS_PER_FOOT * float(input("Input distance d1 in yards: "))
d2 = float(input("Input distance d2 in feet: "))
h = YARDS_PER_FOOT * float(input("Input h in yards: "))
v_sand = FETT_PER_MILE * float(input("Input speed v_sand in m/h: ")) / SECONDS_PER_HOUR
n = float(input("Input n cofficient: "))
theta1 = float(input("Input angel in deegres: ")) / DEGREES_PER_RADIAN

L1 = d1 / math.cos(theta1)
x = L1 * math.sin(theta1)

if x > h:
    print("Input angel is to big")
else:
    L2 = math.sqrt((h-x)**2 + d2**2)
    time = L1 / v_sand + L2 / (v_sand/n)
    print(f"Rescuer will save drowning human after: %.1f seconds" %time)
    