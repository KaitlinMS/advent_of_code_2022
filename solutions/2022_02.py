# A = rock
# B = paper
# C = scissors

# X = rock
# Y = paper
# Z = scissors

# Rock = 1 pt
# Paper = 2 pt
# Scissors = 3 pt
point_values = {'X': 1, 'Y': 2, 'Z': 3}

# Loss = 0 pts
# Draw = 3 pts
# Win = 6 pts
win_conditions = ['A Y', 'B Z', 'C X']
loss_conditions = ['A Z', 'B X', 'C Y']
draw_conditions = ['A X', 'B Y', 'C Z']

dataset = '../puzzle_data/2022_02.txt'
score = 0

with open(dataset) as file:
    for index, line in enumerate(file):
        stripped_line = line.strip()
        opponent_move, my_move = stripped_line.split()

        if stripped_line in win_conditions:
            score = score + 6 + point_values[my_move]
        elif stripped_line in loss_conditions:
            score = score + point_values[my_move]
        elif stripped_line in draw_conditions:
            score = score + 3 + point_values[my_move]

print(score)
