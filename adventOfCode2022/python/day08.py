# https://adventofcode.com/2022/day/8

def build_heigth_matrix(heigth_map):
    rows = heigth_map.split("\n")
    matrix = []
    for row in rows:
        matrix.append(list(row))
    
    return matrix

def check_trees_below(matrix, visibility_matrix, row, col):
    visibility_matrix[row][col] = True

    max_heigth = matrix[row][col]
    while row < len(matrix):
        if matrix[row][col] > max_heigth:
            max_heigth = matrix[row][col]
            visibility_matrix[row][col] = True

        row += 1  

def check_trees_above(matrix, visibility_matrix, row, col):
    visibility_matrix[row][col] = True

    max_heigth = matrix[row][col]
    while row > 0:
        if matrix[row][col] > max_heigth:
            max_heigth = matrix[row][col]
            visibility_matrix[row][col] = True

        row -= 1

def check_right_trees(matrix, visibility_matrix, row, col):
    visibility_matrix[row][col] = True

    max_heigth = matrix[row][col]
    while col < len(matrix):
        if matrix[row][col] > max_heigth:
            max_heigth = matrix[row][col]
            visibility_matrix[row][col] = True

        col += 1

def check_left_trees(matrix, visibility_matrix, row, col):
    visibility_matrix[row][col] = True

    max_heigth = matrix[row][col]
    while col > 0:
        if matrix[row][col] > max_heigth:
            max_heigth = matrix[row][col]
            visibility_matrix[row][col] = True

        col -= 1

def count_visible_trees(matrix):
    visibility_matrix = [[False for col in row] for row in matrix]

    row = 0
    while row < len(matrix):
        check_right_trees(matrix, visibility_matrix, row, 0)
        check_left_trees(matrix, visibility_matrix, row, len(matrix[0]) - 1)
        row += 1

    col = 0
    while col < len(matrix[0]):
        check_trees_below(matrix, visibility_matrix, 0, col)
        check_trees_above(matrix, visibility_matrix, len(matrix) - 1, col)
        col += 1

    # print(matrix)
    # print(visibility_matrix)
    num_visible_trees = 0
    for row in visibility_matrix:
        num_visible_trees += row.count(True)
    
    return num_visible_trees

target = 21
heigth_map = """\
30373
25512
65332
33549
35390\
"""
# t t t t t
# t t t f t
# t t f t t
# t f t f t
# t t t t t
# print(build_matrices(heigth_map)[1])

matrix = build_heigth_matrix(heigth_map)
if count_visible_trees(matrix) == target:
    print("Success")
else:
    print(count_visible_trees(matrix))


# return a list of coordinates tuples of valid adjacent trees
# ex: [(row1, col1), (row2, col2)]
# def get_adjacent_trees_coor(matrix, row, col):
#     adjacent_trees = []
#     # not in top border
#     if row != 0:
#         adjacent_trees.append((row - 1, col))
#     # not in bottom border
#     if row != len(matrix) - 1:
#         adjacent_trees.append((row + 1, col))

#     # not in left border
#     if col != 0:
#         adjacent_trees.append((row, col - 1))
#     # not in right border
#     elif col == len(matrix[0]) - 1:
#         adjacent_trees.append((row, col + 1))

#     return adjacent_trees