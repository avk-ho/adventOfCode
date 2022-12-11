# https://adventofcode.com/2022/day/9

# return a list containing (str_direction, int_num) tuples
def format_motions(motions):
    formatted_motions = motions.split("\n")
    result = []
    for motion in formatted_motions:
        motion = motion.split()
        direction, num = motion[0], int(motion[1])
        result.append((direction, num))

    return result


def is_head_adjacent(head_coor, tail_coor):
    head_x, head_y = head_coor[0], head_coor[1]
    tail_x, tail_y = tail_coor[0], tail_coor[1]

    return abs(head_x - tail_x) < 2 and abs(head_y - tail_y) < 2


def count_visited_tail_positions(motions):
    motions = format_motions(motions)
    # print(motions)

    head = [0, 0]
    tail = [0, 0]
    visited_positions = {(0, 0)}

    for motion in motions:
        direction, num = motion[0], motion[1]

        while num > 0:
            head_prev_coor = head.copy()

            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "R":
                head[0] += 1

            if not is_head_adjacent(head, tail):
                tail = head_prev_coor
                visited_positions.add(tuple(tail))

            num -= 1
    
    # print(visited_positions)
    return len(visited_positions)


target = 13
motions = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2\
"""

if count_visited_tail_positions(motions) == target:
    print("Success")
else:
    print(count_visited_tail_positions(motions))