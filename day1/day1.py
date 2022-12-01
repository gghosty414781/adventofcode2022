# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:26:23 2022

@author: Gareth
"""

biggest_calories = 0
current_calories = 0

with open('day1.txt') as f:
    for line in f:
        
        if current_calories > biggest_calories:
            biggest_calories = current_calories
            
        if line == '\n':
            current_calories = 0
        else:
            current_calories += int(line.strip())

print (biggest_calories)