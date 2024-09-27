def comparison_with_dict(dictionary, temp_str, temp_arr, condition):
    for x in dictionary.keys():
        if temp_str == str(x):      # if temp.__contains__(x) by bolo dobre iba pre max 3 pismena
            temp_arr.append(dictionary[str(x)])
            condition = True
            break
        
    return condition

def count_numbers(string_numbers=False):
    all_lines_numbers = []

    with open(path_to_file, "r") as myFile:
        for line in myFile:
            temp_array = []
            if string_numbers == False:
                for character in line:
                    if character.isdigit() == True:
                        temp_array.append(character)
                all_lines_numbers.append(temp_array)
                
            else:
                temp_array = []
                for j in range(len(line)):
                    if line[j].isdigit() == True:
                        temp_array.append(int(line[j]))
                    temp_string = ""
                    found = False
                    
                    for k in range (0, 3):
                        if (j+k) < len(line):
                            temp_string += line[j+k]

                    if (comparison_with_dict(this_dict, temp_string, temp_array, found) == True):
                        continue
                    
                    for k in range (3,5):
                        if (j+k) < len(line):
                            temp_string += line[j+k]
                                
                            if (comparison_with_dict(this_dict, temp_string, temp_array, found) == True):
                                continue
                            
                all_lines_numbers.append(temp_array)            
                
    #print(all_lines_numbers)
    final_sum = 0
        
    for each in all_lines_numbers:
        if len(each) != 0:
            temp_for_sum = str(each[0]) + str(each[-1])
            final_sum += int(temp_for_sum)

    print(f"Sum of numbers is {final_sum}.")


#count_numbers()

path_to_file = ""
this_dict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
count_numbers(string_numbers=True)

        