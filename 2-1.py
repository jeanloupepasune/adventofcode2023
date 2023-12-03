#!/usr/bin/env python3

from re import findall as findall

with open("2-1.input") as pb_input:
    valid_game_ids_sum = 0
    for line in pb_input.readlines():
        line = line.strip()
        data = line.split(':')
        game_id = int(data[0].replace('Game ', ''))
        data = data[1]
        red_values = [ int(x) for x in findall(r'(\d+) red', data) ]
        green_values = [ int(x) for x in findall(r'(\d+) green', data) ]
        blue_values = [ int(x) for x in findall(r'(\d+) blue', data) ]
        if (all(x<=12 for x in red_values) and
            all(x<=13 for x in green_values) and
            all(x<=14 for x in blue_values)):
            # let's add our valid game id
            valid_game_ids_sum += game_id
    print("The sum of all valid game ids is: ", valid_game_ids_sum)
