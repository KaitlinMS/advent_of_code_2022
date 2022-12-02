dataset = '../puzzle_data/2022_01.txt'

highest_calories = 0
current_count = 0
top_3_calorie_counts = []

with open(dataset, 'r') as file:
    for line in file:
        if line != '\n':
            current_count = current_count + int(line)
        else:
            top_3_calorie_counts.append(current_count)
            top_3_calorie_counts.sort(reverse=True)

            current_count = 0

            if len(top_3_calorie_counts) > 3:
                top_3_calorie_counts.pop(3)

# We need to add the final line in the file too!
top_3_calorie_counts.append(current_count)
top_3_calorie_counts.sort(reverse=True)
top_3_calorie_counts.pop(3)

print(top_3_calorie_counts)
print(top_3_calorie_counts[0])
print(sum(top_3_calorie_counts))


