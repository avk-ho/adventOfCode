# https://adventofcode.com/2022/day/12

import copy

def create_matrix(map):
    formatted_map = map.split("\n")
    matrix = [list(row) for row in formatted_map]
    
    return matrix


def create_num_matrix(matrix):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_dict = {char: idx for idx, char in enumerate(alphabet)}

    num_matrix = []
    for row in matrix:
        num_row = []
        for char in row:
            if char == "S":
                num_row.append(alphabet_dict["a"])
            elif char == "E":
                num_row.append(alphabet_dict["z"])
            else:
                num_row.append(alphabet_dict[char])
        num_matrix.append(num_row)
    
    return num_matrix


def find_start_end(matrix):
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == "S":
                start = (i, j)
            elif char == "E":
                end = (i, j)

    return (start, end)


def count_min_moves(height_map):
    # return a list of (row, col) tuples of potential moves
    # ex: [(1, 0), (0, 1)]
    def find_next_moves(bool_matrix, coor):
        next_moves = []
        row, col = coor[0], coor[1]

        if row != 0:
            if not bool_matrix[row - 1][col] and \
                    num_matrix[row - 1][col] <= num_matrix[row][col] + 1:
                next_moves.append((row - 1, col))
        if row != len(bool_matrix) - 1:
            if not bool_matrix[row + 1][col] and \
                    num_matrix[row + 1][col] <= num_matrix[row][col] + 1:
                next_moves.append((row + 1, col))

        if col != 0:
            if not bool_matrix[row][col - 1] and \
                    num_matrix[row][col - 1] <= num_matrix[row][col] + 1:
                next_moves.append((row, col - 1))
        if col != len(bool_matrix[0]) - 1:
            if not bool_matrix[row][col + 1] and \
                    num_matrix[row][col + 1] <= num_matrix[row][col] + 1:
                next_moves.append((row, col + 1))

        return next_moves

    # recursive function, checks potential moves, and "advance" to those
    # coordinates, while keeping track of previously explored coordinates,
    # adds number of moves taken to paths if target position is reached
    def advance(current_coor, bool_matrix, nb_moves):
        bool_matrix[current_coor[0]][current_coor[1]] = True
        # print(visited_matrix)
        next_moves = find_next_moves(bool_matrix, current_coor)
        # print(next_moves)
        if len(next_moves) == 0:
            return
        if end in next_moves:
            paths.append(nb_moves + 1)
            return
        else:
            for coor in next_moves:
                advance(coor, copy.deepcopy(bool_matrix), nb_moves + 1)

    
    matrix = create_matrix(height_map)
    start, end = find_start_end(matrix)
    num_matrix = create_num_matrix(matrix)
    # print(num_matrix)
    # print(start, end)
    visited_matrix = [[False for col in row] for row in matrix]
    paths = []
    advance(start, copy.deepcopy(visited_matrix), 0)
    # print(paths)
    # print(visited_matrix)

    if len(paths) == 0:
        return -1
    else:
        return min(paths)


target = 31
height_map = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi\
"""

if count_min_moves(height_map) == target:
    print("Success")
else:
    print(count_min_moves(height_map))