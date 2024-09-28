import re
import numpy as np

def findWinningNumbers(winning_nums, given_nums):
    temp_points = 0
    copies_of_active_card = amounts_of_cards[line_index]
    for i in given_nums:
        for j in winning_nums:
            if i == j:
                #print(f"found winning number: {i}!")
                temp_points += 1
                amounts_of_cards[line_index+temp_points] += (1 * copies_of_active_card)

    #print(amounts_of_cards)
    points = int(2**(temp_points-1))  #musi byt int, lebo negativne exponenty to pokazia
    return points


TEXTFILE = "winning_cards.txt"
# ----- LENGHT of a textifle ----- #
with open(TEXTFILE) as f:
    len_of_lines = len(f.readlines())

amounts_of_cards = np.ones(len_of_lines, dtype=int)

total_points = 0
with open(TEXTFILE, 'r') as myFile:
    line_index = -1
    while True:
        line = myFile.readline().rstrip()
        line_index += 1
        if not line: 
            break
               
        win, giv = line.split('|')
        # moze byt iba win.split()
        winning = re.findall(r"[\w']+", win)
        for i in range(0,2):
            winning.pop(0)
        given = re.findall(r"[\w']+", giv)

        total_points += findWinningNumbers(winning, given)

print(f"Total amount of points within the cards = {total_points}")
print(f"Total amount of owned cards = {np.sum(amounts_of_cards)}")
