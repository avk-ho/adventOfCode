# https://adventofcode.com/2022/day/4

def count_fully_contain_pairs(assignments):
    formatted_assignments = format_assignments(assignments)
    
    nb_overlap = 0
    for pair in formatted_assignments:
        elf1, elf2 = pair[0], pair[1]
        start1, start2 = elf1[0], elf2[0]
        end1, end2 = elf1[1], elf2[1]

        outcome_key = ""
        if start1 == start2:
            outcome_key += "0"
        elif start1 > start2:
            outcome_key += "1"
        elif start1 < start2:
            outcome_key += "2"

        if end1 == end2:
            outcome_key += "0"
        elif end1 > end2:
            outcome_key += "1"
        elif end1 < end2:
            outcome_key += "2"

        # print(outcome_key)
        if outcomes[outcome_key]:
            nb_overlap += 1

    return nb_overlap


def format_assignments(assignments):
    formatted_pairs = assignments.split("\n")
    # print(formatted_pairs)
    
    final_format = []
    for pair in formatted_pairs:
        pair = pair.split(", ")
        # print(pair)

        first_assignment, second_assignment = pair[0], pair[1]
        first_assignment, second_assignment = first_assignment.split("-"), second_assignment.split("-")
        # print(first_assignment, second_assignment)

        final_format.append((first_assignment, second_assignment))
    
    # print(final_format)
    return final_format


outcomes = {
    "00": True,
    "01": True,
    "02": True,
    "10": True,
    "11": False,
    "12": True,
    "20": True,
    "21": True,
    "22": False,
}

assignments = """\
2-4, 6-8
2-3, 4-5
5-7, 7-9
2-8, 3-7
6-6, 4-6
2-6, 4-8\
"""

print(count_fully_contain_pairs(assignments))