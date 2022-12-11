with open('11/input.txt') as f:
    lines = f.readlines()


def parse_monkeys(lines):
    monkeys = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('Monkey'):
            items = list(map(int, lines[i + 1].split(':')[1].split(',')))
            operation = lines[i + 2].split('=')[1].strip()
            test_div = int(lines[i + 3].split('by')[1].strip())
            true_target = int(lines[i + 4].split('monkey')[1].strip())
            false_target = int(lines[i + 5].split('monkey')[1].strip())
            monkeys.append({
                'items': items,
                'operation': operation,
                'test_div': test_div,
                'true_target': true_target,
                'false_target': false_target,
                'inspections': 0
            })
            i += 7
        else:
            i += 1
    return monkeys


def apply_operation(old, operation):
    if operation == 'old * old':
        return old * old
    parts = operation.split()
    if parts[1] == '*':
        return old * int(parts[2])
    else:
        return old + int(parts[2])


def simulate_rounds(monkeys, rounds, divide_by_three=True):
    # Product of all test divisors keeps worry bounded while preserving divisibility checks
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey['test_div']
    
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey['items']:
                item = monkey['items'].pop(0)
                worry = apply_operation(item, monkey['operation'])
                # Part 1: relief after inspection divides worry by 3
                if divide_by_three:
                    worry //= 3
                worry %= modulo
                if worry % monkey['test_div'] == 0:
                    monkeys[monkey['true_target']]['items'].append(worry)
                else:
                    monkeys[monkey['false_target']]['items'].append(worry)
                monkey['inspections'] += 1


def solve_part_1(lines):
    monkeys = parse_monkeys(lines)
    simulate_rounds(monkeys, 20, divide_by_three=True)
    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    result = inspections[0] * inspections[1]

    print(f"Part 1 Solution: {result}")


def solve_part_2(lines):
    monkeys = parse_monkeys(lines)
    simulate_rounds(monkeys, 10000, divide_by_three=False)
    inspections = sorted([m['inspections'] for m in monkeys], reverse=True)
    result = inspections[0] * inspections[1]
    
    print(f"Part 2 Solution: {result}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)