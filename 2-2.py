#!/usr/bin/env python3

from re import findall as findall

with open("2-2.input") as pb_input:
    set_power_sum = 0
    for line in pb_input.readlines():
        line = line.strip()
        data = line.split(':')[1]
        red_values = [ int(x) for x in findall(r'(\d+) red', data) ]
        green_values = [ int(x) for x in findall(r'(\d+) green', data) ]
        blue_values = [ int(x) for x in findall(r'(\d+) blue', data) ]
        set_power_sum += max(red_values) * max(blue_values) * max(green_values)
    print("The sum of the powers of all minimum sets is: ", set_power_sum)
