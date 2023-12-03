#!/usr/bin/env python3

with open("1-1.input") as pb_input:
    calibration_sum = 0
    for line in pb_input.readlines():
        chars = list(line)
        firstd = 0
        lastd = 0
        for c in chars:
            # quick and dirty: try to cast to an int.
            # if it fails (example: cannot cast 'a' string litteral to int)
            # just ignore and go on.
            # could also import re... :-)
            try:
                if int(c) in range(0,10):
                    firstd = int(c)
                    break
            except:
                pass
        for c in chars[::-1]:
            try:
                if int(c) in range(0,10):
                    lastd = int(c)
                    break
            except:
                pass
        calibration_value = firstd * 10 + lastd
        calibration_sum += calibration_value
    print("Sum of all calibration values: ", calibration_sum)
