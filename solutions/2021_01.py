import file_processor

dataset = '../puzzle_data/2021_01.txt'

# ----- PART 1 ----- #

increases = 0
depths_strings = file_processor.process_file(dataset)
depths = [int(s) for s in depths_strings]

for i in range(len(depths)):
    if depths[i] > depths[i - 1]:
        increases = increases + 1

print('The depth increases ' + str(increases) + ' times')

# ----- PART 2 ----- #

window_a = 0
window_b = 0
window_increases = 0

for i in range(len(depths)):
    try:
        window_a = depths[i] + depths[i + 1] + depths[i + 2]
        window_b = depths[i + 1] + depths[i + 2] + depths[i + 3]

        if window_b > window_a:
            window_increases = window_increases + 1
    except IndexError:
        break

print('The number of window increases is ' + str(window_increases))