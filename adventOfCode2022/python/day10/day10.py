# https://adventofcode.com/2022/day/10

from day10_program import program

def format_program(program):
    commands = program.split("\n")
    formatted_program = []
    for command in commands:
        if command != "noop":
            command = command.split()
            command = (command[0], int(command[1]))

        formatted_program.append(command)
    
    return formatted_program


def sum_of_signal_strengths(cycles, program):
    formatted_program = format_program(program)
    cycles = cycles.copy()
    cycle = 0
    x = 1
    signal_strengths = []

    while len(cycles) > 0:
        target = cycles.pop(0)
        signal_strength = None
        while cycle < target:
            command = formatted_program.pop(0)
            
            cycle += 1
            if command != "noop":
                cycle += 1
                if cycle >= target:
                    signal_strength = target * x
                    # print(f"inloop {target} * {x}")
                x += command[1]
        
        if signal_strength is None:
            signal_strength = target * x
            # print(f"outloop {target} * {x}")

        # print(f"cycle: {cycle}")
        # print(signal_strengths)
        signal_strengths.append(signal_strength)

    return sum(signal_strengths)


# print(format_program(program))
cycles_to_check = [20 + num*40 for num in range(6)]
# print(cycles_to_check)
target = 13140

if sum_of_signal_strengths(cycles_to_check, program) == target:
    print("Success")
else:
    print(sum_of_signal_strengths(cycles_to_check, program))