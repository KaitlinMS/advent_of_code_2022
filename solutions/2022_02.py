# A = rock
# B = paper
# C = scissors
# X = rock / lose
# Y = paper / draw
# Z = scissors / win

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
part_1_score = 0
part_2_score = 0

with open(dataset) as file:
    for index, line in enumerate(file):
        stripped_line = line.strip()
        opponent_move, my_move = stripped_line.split()

        # PART 1
        if stripped_line in win_conditions:
            part_1_score = part_1_score + 6 + point_values[my_move]
        elif stripped_line in loss_conditions:
            part_1_score = part_1_score + point_values[my_move]
        elif stripped_line in draw_conditions:
            part_1_score = part_1_score + 3 + point_values[my_move]

        # PART 2
        if my_move == 'X':  # I need to lose
            move_set = [i for i in loss_conditions if opponent_move in i]
            opponent_shape, my_shape = move_set[0].split()
            part_2_score = part_2_score + point_values[my_shape]
        elif my_move == 'Y':  # I need to draw
            move_set = [i for i in draw_conditions if opponent_move in i]
            opponent_shape, my_shape = move_set[0].split()
            part_2_score = part_2_score + 3 + point_values[my_shape]
        elif my_move == 'Z':  # I need to win
            move_set = [i for i in win_conditions if opponent_move in i]
            opponent_shape, my_shape = move_set[0].split()
            part_2_score = part_2_score + 6 + point_values[my_shape]

print(part_1_score)
print(part_2_score)
