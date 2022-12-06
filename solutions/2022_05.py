import numpy

dataset = '../puzzle_data/2022_05_sample.txt'
stacks = []
columns = 3  # I can easily tell this from looking at the data

with open(dataset) as file:
    for index, line in enumerate(file):
        # Ignore the column labels and the empty line
        # But make sure to check for empty lines first to avoid a crash
        if line == '\n' or line.strip()[0].isdigit():
            continue

        elif line.startswith('move'):
            instructions = line.split()  # [move, X, from, Y, to, Z]
            moves = int(instructions[1])
            current_row = 0

            # Subtracting 1 because arrays are zero indexed
            start_col = int(instructions[3]) - 1
            end_col = int(instructions[5]) - 1

            print('Instruction:')
            print(line)

            # range starts at 0 and ends at moves-1
            for move in range(moves):
                # Find the top of the column
                if stacks[current_row][end_col] == '[*]':
                    current_row += 1
                    continue

                moving_item = stacks[current_row][start_col]
                stacks[current_row][start_col] = '[*]'

                stacks[current_row][end_col] = moving_item

        else:
            # I'm using [*] to denote an empty spot
            # Then I'm splitting each item in the stack so that this becomes a 2D array
            stacks.append(line.replace('   ', '[*]').split())

            # We need to pad out the array with empty spaces on the right side now
            while len(stacks[index]) < columns:
                stacks[index].append('[*]')

        print('Stacks:')
        print(numpy.matrix(stacks))
        print()

