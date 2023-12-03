#!/usr/bin/env python3

# naughty elves made me import re eventually
from re import findall as findall

ugly_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        # yes, it does go on
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        # ...and on!
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
        # lol
        }

with open("1-1.input") as pb_input:
    calibration_sum = 0
    for line in pb_input.readlines():
        # beware of the overlap! lookahead (?=...) needed to deal with oneight and co.
        numbers_list = findall(
                r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))',
                line
                )
        numbers_list = [ ugly_dict[n] for n in numbers_list ]
        
        calibration_sum += numbers_list[0] * 10 + numbers_list[-1]
    print("Sum of all calibration values: ", calibration_sum)
