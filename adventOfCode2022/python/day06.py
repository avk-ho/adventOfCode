# https://adventofcode.com/2022/day/6

def find_start_of_packet(datastream):
    current_idx = 4
    characters = [char for idx, char in enumerate(datastream) if idx < 4]
    valid_start = is_valid(characters)

    while not valid_start and current_idx < len(datastream)-4:
        characters.pop(0)
        characters.append(datastream[current_idx])

        if is_valid(characters):
            valid_start = True

        current_idx += 1

    return current_idx


# return True if all 4 characters in array are uniques, else False
def is_valid(array):
    length = len(set(array))
    return length == 4


datastream1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # 7
datastream2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"  # 5
datastream3 = "nppdvjthqldpwncqszvftbrmjlhg"  # 6
datastream4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"  # 10
datastream5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # 11

results = []
ds1 = find_start_of_packet(datastream1)
results.append(ds1)
if not (ds1 == 7):
    print(f"ds1: {ds1}")

ds2 = find_start_of_packet(datastream2)
results.append(ds2)
if not (ds2 == 5):
    print(f"ds2: {ds2}")

ds3 = find_start_of_packet(datastream3)
results.append(ds3)
if not (ds3 == 6):
    print(f"ds3: {ds3}")

ds4 = find_start_of_packet(datastream4)
results.append(ds4)
if not (ds4 == 10):
    print(f"ds4: {ds4}")

ds5 = find_start_of_packet(datastream5)
results.append(ds5)
if not (ds5 == 11):
    print(f"ds5: {ds5}")

for result in results:
    print(result)
