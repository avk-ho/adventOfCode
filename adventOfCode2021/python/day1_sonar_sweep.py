# https://adventofcode.com/2021/day/1

def sonarSweep(report):
    counter = 1
    max = len(report)
    increaseCount = 0

    while counter < max:
        if report[counter] > report[counter-1]:
            increaseCount += 1
    counter += 1

    return increaseCount