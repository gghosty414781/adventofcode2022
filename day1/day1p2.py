# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:26:23 2022

@author: Gareth
"""

biggest_calories = [0, 0, 0]
current_calories = 0

with open('day1.txt') as f:
    for line in f:
        
        biggest_calories.sort()                                                 #.sort function arranges them from smallest to largest
        if current_calories > biggest_calories[0]:
            biggest_calories[0] = current_calories
            
        if line == '\n':                                                        # \n is empty line
            current_calories = 0
        else:
            current_calories += int(line.strip())                               # .strip() is the current line

print (sum(biggest_calories))
