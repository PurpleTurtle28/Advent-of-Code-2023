import numpy as np

textfile = ""

def fileShape():
    myFile = open(textfile, 'r')
    file_shape = len(myFile.readlines())
    myFile.close()

    return file_shape


def findSymbols():
    array_of_symbols = set()

    myFile = open(textfile, 'r')
    for char in myFile.read():         #.rstrip() nefunguje
        if char.isnumeric() == False and char != '.':
            array_of_symbols.add(char)
    array_of_symbols.discard('\n')
    
    myFile.close()

    return array_of_symbols


def searchForSymbols_basedOnRestrictions(array_of_positions, first_number, last_number, line_index, validNumber=False):
    symbolFound = False
    while first_number <= last_number:
        for symbol in symbols:
            if array_of_positions[first_number] == symbol:
                #print(f"found symbol {symbol} on position {first_number}, line {line_index}")
                if symbol == '*':
                    array_of_gear_numbers.append([line_index, first_number, int(number)])
                symbolFound = True
                validNumber = True
                break
        if symbolFound != True:
            first_number += 1
        else:
            break
        
    return validNumber
    

def searchForSymbols(array_of_positions, line_index):
    if len(array_of_positions) != 0:
        if first_number_index != 0 and last_number_index != len(array_of_positions)-1:
            return searchForSymbols_basedOnRestrictions(array_of_positions, first_number_index-1, last_number_index+1, line_index) 

        elif first_number_index == 0:
            return searchForSymbols_basedOnRestrictions(array_of_positions, first_number_index, last_number_index+1, line_index) 

        elif last_number_index != len(array_of_positions):
            return searchForSymbols_basedOnRestrictions(array_of_positions, first_number_index-1, last_number_index, line_index) 


def surrounding_line_lower():
    lower = list()
    if i != len(array_of_lines)-1:
        for j in array_of_lines[i+1][0]:
            lower.append(j)
    
    return lower

def surrounding_line_upper():
    upper = list()  
    if i != 0:
        for j in array_of_lines[i-1][0]:
            upper.append(j)

    return upper


def summingExactlyTwoNumbers(array_of_stars):
    pairs = list()
    conjoined = np.ndarray(shape=(len(array_of_stars),1),dtype=object)
    for elem in range(len(array_of_stars)):
        conjoined[elem] = str(array_of_stars[elem][0]) + str(array_of_stars[elem][1])
    
    for first_elem in range(len(conjoined)):
        counter = [first_elem]
        for elem in range(len(conjoined)):
            if first_elem != elem and conjoined[first_elem] == conjoined[elem]:
                counter.append(elem)
        if len(counter) == 2:
            pairs.append(array_of_stars[counter[0]][2] * array_of_stars[counter[1]][2])  
            counter.clear()
            conjoined[first_elem] = 0
        else:
            for i, value in enumerate(counter):
                conjoined[value] = 0
            counter.clear()

    return np.sum(pairs)


array_of_lines = np.ndarray(shape=(fileShape(),1),dtype=object)
array_of_valid_numbers = list()
array_of_gear_numbers = list()

with open(textfile, 'r') as myFile:
    i = 0
    while True:
        line = myFile.readline().rstrip()
        #print(line)    
        if not line: 
            break
        
        array_of_lines[i] = line
        i += 1

symbols = findSymbols()


for i in range(0, len(array_of_lines)):

    current_line = list()
    print(f"Line {i+1}")
    for j in array_of_lines[i][0]:
        current_line.append(j)

    DoWeGotaNumberInTheFirstPlace = False
    first_number_index = -1
    last_number_index = -1

    for index, elem in enumerate(current_line):
        if last_number_index >= index:
            continue
        else:
            number = ''
            # If you find a number, continue with searching the next indecies until there is no other number to append
            if elem.isnumeric() == True:
                DoWeGotaNumberInTheFirstPlace = True
                first_number_index = index
                last_number_index = index
                number += elem

                next = 1
                while current_line[index+next].isnumeric() == True:
                    last_number_index = index+next
                    number += current_line[index+next]
                    next += 1
                    if index+next == len(current_line):
                        break
            
            # When you find the whole number, continue with searching for adjascent symbols
            if DoWeGotaNumberInTheFirstPlace == True:
                
                if searchForSymbols(array_of_lines[i][0], i) == True:
                    print(f"number {number} is valid\n")
                    array_of_valid_numbers.append(int(number))
                    DoWeGotaNumberInTheFirstPlace = False
                    continue

                lower = surrounding_line_lower()
                lower_line_index = i+1
                upper = surrounding_line_upper()
                upper_line_index = i-1

                if searchForSymbols(lower, lower_line_index) == True or searchForSymbols(upper, upper_line_index) == True:
                    print(f"number {number} is valid\n")
                    array_of_valid_numbers.append(int(number))

            DoWeGotaNumberInTheFirstPlace = False

print(f"Sum of all valid numbers is {np.sum(array_of_valid_numbers)}.\n")

print(f"Sum of pairs of valid numbers with gear is {summingExactlyTwoNumbers(array_of_gear_numbers)}.\n")
