# https://adventofcode.com/2022/day/3

def sum_of_item_priority(rucksacks, priority):
    rucksacks = rucksacks.split("\n")
    # print(rucksacks)

    sum_of_priorities = 0
    for rucksack in rucksacks:
        item = find_misplaced_item(rucksack)
        sum_of_priorities += priority.index(item)

    return sum_of_priorities    

def find_misplaced_item(rucksack):
    compartiments = divide_compartiments(rucksack)
    item = compartiments[0] & compartiments[1]
    item = list(item)
    
    # print(item)
    return item[0]

def divide_compartiments(rucksack):
    rucksack = list(rucksack)
    half_idx = int(len(rucksack)/2)
    compartiment1, compartiment2 = set(rucksack[:half_idx]), set(rucksack[half_idx:])
    
    # print(compartiment1, compartiment2)
    return compartiment1, compartiment2


lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = lowercase_alphabet.upper()
priority = ["0"]
for character in lowercase_alphabet:
    priority.append(character)
for character in uppercase_alphabet:
    priority.append(character)
# print(priority)

rucksacks = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw\
"""

# print(rucksacks)
print(sum_of_item_priority(rucksacks, priority))