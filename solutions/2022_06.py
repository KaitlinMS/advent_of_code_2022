from collections import Counter

dataset = '../puzzle_data/2022_06.txt'


def find_sequence(num_characters):
    with open(dataset) as file:
        for line in file:
            # Look at sequences of 4 characters at a time
            for i in range(0, len(line)):
                end = i + num_characters
                sequence = line[i:end]  # this is called 'slicing'

                # Check if this sequence has repeated characters
                count_chars = Counter(sequence)

                if any([True for k, v in count_chars.items() if v > 1]):
                    continue
                else:
                    print('Sequence found!')
                    print('Position: ' + str(i))
                    print('Sequence: ' + sequence)
                    print('Number of characters processed: ' + str(i + num_characters))
                    print()
                    break


find_sequence(4)
find_sequence(14)
