# https://adventofcode.com/2022/day/5

def check_top_of_stacks(crate_stacks, instructions):
    formatted_instructions = format_instructions(instructions)

    for instruction in formatted_instructions:
        num_of_crates = instruction[0]
        origin, destination = instruction[1], instruction[2]
        while num_of_crates > 0:
            move_to_stack(crate_stacks, origin, destination)

            num_of_crates -= 1

    message = ""
    for stack in crate_stacks.values():
        top_crate = stack.pop()
        message += top_crate

    return message

# move the crate at the top of the origin stack to the top of destination stack
def move_to_stack(crate_stacks, origin, destination):
    crate = crate_stacks[origin].pop()
    crate_stacks[destination].append(crate)


# return a list of tuples containing in order: 
# number of crates to move, origin of the crates, destination of the move
# ex: [(1, 2, 1), (3, 1, 3)]
def format_instructions(instructions):
    formatted_instructions = []
    instructions = instructions.split("\n")

    for instruction in instructions:
        instruction = instruction.split()
        nb = (int(instruction[1]), instruction[3], instruction[5])
        formatted_instructions.append(nb)

    return formatted_instructions

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
crate_stacks = {
    "1": ["Z", "N"],
    "2": ["M", "C", "D"],
    "3": ["P"]
}
instructions = """\
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2\
"""

print(check_top_of_stacks(crate_stacks, instructions))