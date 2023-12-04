#!/usr/bin/env python3

from re import findall

with open("4-1.input") as pb_input:
    total_card_score = 0
    for line in pb_input.readlines():
        win_count = 0
        numbers = line.strip().split(':')[1].split('|')
        winning_numbers = numbers[0].split()
        played_numbers = numbers[1].split()
        for n in played_numbers:
            if n in winning_numbers:
                win_count += 1
        if win_count > 0:
            total_card_score += 2**(win_count -1)
    print('Total card score is: ', total_card_score)
