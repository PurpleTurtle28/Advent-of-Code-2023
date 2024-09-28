def beating_record(duration, record):

    no_ways_to_beat_record = 0
    possible_holding_time = duration - 1

    if (duration - 1) % 2 == 0:
        hold = int(possible_holding_time/2)
    else:
        hold = int((possible_holding_time+1)/2)

    for actual in range(1, duration):
        if actual > hold:
            break
        eq = (duration - actual) * actual
        #print(f"Holding button for {actual} s; boat travels {eq} mm.")
        
        if eq > record:
            #print("...which is better than high score")
            if actual == hold and possible_holding_time % 2 == 1:
                no_ways_to_beat_record += 1            
            else:
                no_ways_to_beat_record += 2            

    return no_ways_to_beat_record

more_races = False
TEXTFILE = "boats_races.txt"

with open(TEXTFILE, 'r') as myFile:
    line_index = 0
    while True:
        line = myFile.readline()
        if not line: 
            break

        if line.startswith("#") or len(line) == 1:          #if line is empty
            line_index -= 1
            pass

        elif line_index == 0:
            race_durations = line.split()
            race_durations.pop(0)
            if more_races == False:
                race_durations = ''.join(string for string in race_durations)
        elif line_index == 1:
            high_score = line.split()
            high_score.pop(0)
            if more_races == False:
                high_score = ''.join(string for string in high_score)

        line_index += 1

total_number = 1
if more_races == True:
    for i in range(0, len(race_durations)):
        total_number *= beating_record(int(race_durations[i]), int(high_score[i]))
else:
    total_number = beating_record(int(race_durations), int(high_score))

print(f"All numbers multipied = {total_number}")
