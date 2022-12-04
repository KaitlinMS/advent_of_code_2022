import file_processor

dataset = '../puzzle_data/2022_04.txt'

data = file_processor.process_file(dataset)
subsets = 0
overlaps = 0

for ranges in data:
    ranges = ranges.strip()

    left, right = ranges.split(',')

    # range()'s end isn't inclusive, so I'm adding 1 to the "stop" number.
    l1, l2 = left.split('-')
    r1, r2 = right.split('-')
    left_range = range(int(l1), int(l2)+1)
    right_range = range(int(r1), int(r2)+1)

    # Check for fully contained ranges
    if (set(left_range).issubset(right_range)) or (set(right_range).issubset(left_range)):
        subsets = subsets + 1

    # Check for overlaps
    if set(left_range) & set(right_range):
        overlaps = overlaps + 1

print(subsets)
print(overlaps)