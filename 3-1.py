#!/usr/bin/env python3

import re

plan = [] # a list of lists of characters: [['.', '2', '#'], ['4', '.', '.']]
numbers_data = [] # a list of tuples [(number, line_index, start_index, end_index)]
valid_numbers_sum = 0

def get_neighbours(number, line_index, start, end, plan):
    max_y = len(plan)-1
    return (
        # I'm so sorry...                   end of number + 1 (neighbour) + 1  (slicing)
        # min/max to handle edge cases... poorly!
        plan[max(line_index-1, 0)][max(start-1, 0):min(end+1+1, len(plan[line_index]))] +
        plan[line_index][max(start-1, 0):min(end+1+1, len(plan[line_index]))] +
        plan[min(line_index+1, max_y)][max(start-1, 0):min(end+1+1, len(plan[line_index]))]
        )

with open("3-1.input") as pb_input:
    line_index=0
    for line in pb_input.readlines():
        plan.append(list(line.strip()))
        numbers = re.finditer(r'[0-9]+', line)
        for n in numbers:
            numbers_data.append((int(n.group()), line_index, n.span()[0], n.span()[1] - 1))
        line_index += 1
    for n in numbers_data:
        if any([ re.match(r'[^0-9\.]', x) for x in get_neighbours(*n, plan)]):
            valid_numbers_sum += n[0]
            print("valid number: ", n[0], " neighbours: ", get_neighbours(*n, plan))
        else:
            print("invalid number: " , n[0], " neighbours: ", get_neighbours(*n, plan))
    print("Sum of all numbers neighbouring a special character: ", valid_numbers_sum)
