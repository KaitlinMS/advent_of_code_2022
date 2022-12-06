dataset = '../puzzle_data/2022_05_sample.txt'
stacks = []
rotated_stacks = []
columns = 3


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
            stacks.append(line.replace('   ', '[-]').split())

            # Let's also add empty space padding to the end of the lists to ensure they're all the same size
            while len(stacks[index]) < columns:
                stacks[index].append('[-]')

    # Now we need to rotate this sucker so that we can easily append and pop items
        rotated_stacks = stacks
        for row in rotated_stacks:
            print(row)


            for item in reversed(row):
                print(item)




def make_moves(data):
    with open(data) as file:
        for index, line in enumerate(file):
            # We can ignore everything that doesn't start with move
            if not line.startswith('move'):
                continue
            else:
                instructions = line.split()  # [move, X, from, Y, to, Z]


reversed_stacks = build_stacks(dataset)
print('Initial setup:')
# print_stacks(reversed_stacks)
