# https://adventofcode.com/2022/day/1

def findMostCalories(lst):
    max_calories = 0
    # max_elf = 0
    
    for elf, food in enumerate(lst):
        if sum(food) > max_calories:
            # max_elf = elf
            max_calories = sum(food)
    
    return max_calories


lst = [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

print(findMostCalories(lst))