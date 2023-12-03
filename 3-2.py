#!/usr/bin/env python3

from re import finditer as finditer

numbers_data = [] # a list of tuples [(number, line_index, start_index, end_index)]
gearhead_data = [] # a list of tuples [(line_index, gh_index)]
gear_ratio_sum = 0

with open("3-1.input") as pb_input:
    line_index = 0
    for line in pb_input.readlines():
        numbers = finditer(r'[0-9]+', line)
        for n in numbers:
             numbers_data.append(
                     (int(n.group()), line_index, n.span()[0], n.span()[1])
                     )
        gearheads = finditer(r'\*', line)
        for gh in gearheads:
            gearhead_data.append( (line_index, gh.span()[0]) )
        line_index += 1
    # we got our data, let's get neighbouring numbers for every gearhead
    # gh[0]: gearhead line index ; gh[1]: gearhead position index
    # n[0]: number ; n[1]: line index ; n[2]: start index ; **n[3]: stop index +1** (from span())
    for gh in gearhead_data:
        coupling = [
                n[0] for n in numbers_data if (
                    n[1] >= gh[0] - 1 and n[1] <= gh[0] + 1 and
                    n[3] >= gh[1] and n[2] <= gh[1] +1
                    )
                ]
        if len(coupling) == 2:
            gear_ratio_sum += coupling[0] * coupling[1]
    print("Sum of gear ratios: ", gear_ratio_sum)
