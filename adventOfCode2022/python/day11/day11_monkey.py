class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.current_item = None
        self.nb_inspections = 0
        self.operator = ""
        self.operation_arg = 0
        self.test_num = 0
        self.true_monkey_name = ""
        self.false_monkey_name = ""

    def add_item(self, item):
        self.items.append(item)

    def select_next_item(self):
        self.nb_inspections += 1
        self.current_item = self.items.pop(0)

    def set_operation(self, op, arg):
        self.operator = op
        self.operation_arg = arg

    def set_test(self, num, true_monkey, false_monkey):
        self.test_num = num
        self.true_monkey_name = true_monkey
        self.false_monkey_name = false_monkey

    def operation(self):
        arg = self.operation_arg
        if self.operation_arg == "old":
            arg = self.current_item

        if self.operator == "*":
            result = self.current_item * arg
        elif self.operator == "+":
            result = self.current_item + arg
        elif self.operator == "-":
            result = self.current_item - arg
        elif self.operator == "/":
            result = self.current_item / arg

        self.current_item = result // 3

    def test(self, monkeys):
        if self.current_item % self.test_num == 0:
            for monkey in monkeys:
                if monkey.name == self.true_monkey_name:
                    monkey.add_item(self.current_item)
        else:
            for monkey in monkeys:
                if monkey.name == self.false_monkey_name:
                    monkey.add_item(self.current_item)