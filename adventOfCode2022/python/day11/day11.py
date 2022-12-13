# https://adventofcode.com/2022/day/11

from day11_monkey import Monkey


def create_monkeys(notes):
    formatted_notes = notes.split("\n")
    formatted_notes = [note.strip() for note in formatted_notes]
    # print(formatted_notes)
    
    monkeys = []
    idx = 0
    current_monkey = None
    while idx < len(formatted_notes):
        note = formatted_notes[idx]
        # print(note, idx)

        if "Monkey" in note:
            current_monkey = Monkey(note[:-1].lower())
            # print("added name")

        elif note == "":
            monkeys.append(current_monkey)

        elif "Starting items:" in note:
            items = note.split()
            items = items[2:]
            for i, item in enumerate(items):
                if "," in item:
                    item = item[:-1]
                items[i] = int(item)

            for item in items:
                current_monkey.add_item(item)
            # print(f"added items: {items}")

        elif "Operation:" in note:
            operation = note.split()
            operation = operation[4:]
            if operation[1].isnumeric():
                operation[1] = int(operation[1])
            current_monkey.set_operation(operation[0], operation[1])
            # print("added operation")

        elif "Test:" in note:
            test_num = int(note.split()[-1])
            true_complete = False
            false_complete = False
            temp_idx = idx
            while not (true_complete and false_complete):
                temp_idx += 1
                note = formatted_notes[temp_idx]
                if "If true:" in note:
                    true_monkey = note.split("If true: throw to ")[1].lower()
                    true_complete = True
                elif "If false:" in note:
                    false_monkey = note.split("If false: throw to ")[1].lower()
                    false_complete = True

            current_monkey.set_test(test_num, true_monkey, false_monkey)
            # print("added test")

        idx += 1

    monkeys.append(current_monkey)

    # print(monkeys)
    return monkeys

# ilvl -> operation -> // 3 -> test
def count_monkey_business_lvl_after_round(notes, end_round):
    monkeys = create_monkeys(notes)
    # for monkey in monkeys:
    #     print(monkey.name, monkey.items, monkey.operator, monkey.operation_arg, monkey.test_num)
    round = 1

    while round <= end_round:
        for monkey in monkeys: # turn
            while len(monkey.items) > 0:
                monkey.select_next_item()
                monkey.operation()
                monkey.test(monkeys)

        # print(f"round:{round}")
        round += 1
    
    inspections = [monkey.nb_inspections for monkey in monkeys]
    # print(inspections)
    inspections.sort()
    
    return inspections[2] * inspections[3]


target = 10605
notes = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1\
"""


monkeys = create_monkeys(notes)

if count_monkey_business_lvl_after_round(notes, 20) == target:
    print("Success")
else:
    print(count_monkey_business_lvl_after_round(notes, 20))