import numpy

dataset = '../puzzle_data/2022_05.txt'
stacks = []
columns = 9


def print_stacks(stack):
    for row in range(len(stack)):
        print(stack[row])


def build_stacks(data):
    with open(data) as file:
        for index, line in enumerate(file):
            if line.strip()[0].isdigit():
                # We've hit the column labels, and we can now stop reading the file
                break

            # I'm using [-] to denote an empty spot
            # I'm making sure that we don't lose any column information by adding empty spots
            while "    " in line:
                line = line.replace("    ", " [-] ", 1)

            # Convert this into a list
            line = line.split()
            stacks.append(line)

            # Let's also add empty space padding to the end of the lists to ensure they're all the same size
            while len(stacks[index]) < columns:
                stacks[index].append('[-]')

        # Now we need to rotate this sucker so that we can easily append and pop items
        # I'm using numpy because my brain wants to do matrix math, and I'm having a hard time visualizing this
        # in any other way
        rotated_stacks = numpy.array(stacks)
        rotated_stacks = numpy.flipud(rotated_stacks)
        rotated_stacks = numpy.transpose(rotated_stacks)

        # Now let's get this back into a list of lists
        return rotated_stacks.tolist()


def make_moves(data, stack_data, mode='single'):
    # Clean up the empty spaces in the stacks first
    for i in range(0, len(stack_data)):
        stack_data[i] = [j for j in stack_data[i] if j != '[-]']

    print("Initial setup:")
    print_stacks(stack_data)
    print()

    with open(data) as file:
        for line in file:
            # We can ignore everything that doesn't start with move
            if not line.startswith('move'):
                continue
            else:
                instructions = line.split()  # [move, X, from, Y, to, Z]
                moves = int(instructions[1])
                start = int(instructions[3]) - 1  # Minus 1 because of zero-indexing
                finish = int(instructions[5]) - 1  # Minus 1 because of zero-indexing

                if mode == 'single':
                    for i in range(0, moves):
                        moving = stack_data[start].pop()
                        stack_data[finish].append(moving)
                elif mode == 'multi':
                    moving = stack_data[start][-moves:]
                    del stack_data[start][-moves:]
                    stack_data[finish].extend(moving)
                    print("After move:")
                    print(line)
                    print_stacks(stack_data)
                    print()


def get_top_of_stacks(stack_data):
    tops = ''

    for i in range(0, len(stack_data)):
        tops = tops + stack_data[i][-1].strip('[').strip(']')

    print(tops)


stacks = build_stacks(dataset)

print()

make_moves(dataset, stacks, 'multi')

print()

print('Tops of stacks:')
get_top_of_stacks(stacks)
