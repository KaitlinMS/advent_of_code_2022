import file_processor
import string

dataset = '../puzzle_data/2022_03.txt'
data = file_processor.process_file(dataset)
score = 0

# ----- PART 1 -----
for contents in data:
    contents = contents.strip()
    duplicated = ''

    # Split this string into two halves
    half_length = len(contents)//2
    left_half, right_half = contents[:half_length], contents[half_length:]

    # Search for the common item in the contents
    for item in left_half:
        if item in right_half:
            duplicated = item
            break

    # Add one because the index starts at 0 but the score values start at 1
    score = score + string.ascii_letters.index(duplicated) + 1

print(score)

# ----- PART 2 -----
score_2 = 0

for i in range(0, len(data), 3):
    # Get 3 lines at a time
    first = data[i].strip()
    second = data[i+1].strip()
    third = data[i+2].strip()

    for item in first:
        if item in second:
            if item in third:
                score_2 = score_2 + string.ascii_letters.index(item) + 1
                break

print(score_2)