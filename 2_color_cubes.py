import numpy as np

def findAmounts(cube_int, cube_str):
    with open(textfile, "r") as myFile:
        line_number = 0
        for line in myFile:
            line_number += 1
            for i in range(cube_int+1, 21):
                if line.__contains__(f"{i} {cube_str}"):
                    #print(f"found {i} {cube_str} in line {line_number}")
                    false_lines.add(line_number)
                    break


def findMinimums(cube_str):
    with open(textfile, "r") as myFile:
        line_number = 0
        for line in myFile:  
            for i in range(21, 0, -1):
                if line.__contains__(f"{i} {cube_str}"):
                    #print(f"found {i} {cube_str} in line {line_number}")
                    power_array[line_number,index] = i
                    line_number += 1
                    break


def numOfGames():
    file = open(textfile, "r")
    lines = len(file.readlines())
    file.close()

    return lines


textfile = ""

class cube:
    def __init__(self, color, number):
        self.color = color
        self.number = number

red = cube("red", 12)
green = cube("green", 13)
blue = cube("blue", 14)

all_sum = sum(np.linspace(1,numOfGames(),numOfGames()))
false_lines = set()

for c in [red, green, blue]:
    findAmounts(c.number, c.color)
    print(f"impossible games after this run: {false_lines}\n")

print(f"\nSum of possible IDs = {all_sum - sum(false_lines)}")

power_array = np.zeros((numOfGames(),3))

for index, c in enumerate([red, green, blue]):
    findMinimums(c.color)

print(f"\nSum of powers of the thig = {np.sum(np.prod(power_array, axis=1))}")

