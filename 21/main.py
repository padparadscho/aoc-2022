with open('21/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_monkeys(lines):
    monkeys = {}
    for line in lines:
        name, job = line.split(':')
        job = job.strip()
        
        # Number monkey
        if job.isdigit() or (job[0] == '-' and job[1:].isdigit()):
            monkeys[name] = ('number', int(job))
        # Operation monkey
        else:
            parts = job.split()
            monkeys[name] = ('operation', parts[0], parts[1], parts[2])
    
    return monkeys


def evaluate(name, monkeys, humn_value=None):
    job = monkeys[name]
    
    if job[0] == 'number':
        # Special case: humn might need a specific value
        if name == 'humn' and humn_value is not None:
            return humn_value
        return job[1]
    
    # Operation
    _, left, op, right = job
    left_val = evaluate(left, monkeys, humn_value)
    right_val = evaluate(right, monkeys, humn_value)
    
    # Recursively evaluate operations
    if op == '+':
        return left_val + right_val
    elif op == '-':
        return left_val - right_val
    elif op == '*':
        return left_val * right_val
    elif op == '/':
        return left_val // right_val


def solve_part_1(lines):
    monkeys = parse_monkeys(lines)
    result = evaluate('root', monkeys)
    
    print(f"Part 1 Solution: {result}")


def contains_humn(name, monkeys):
    job = monkeys[name]
    
    if job[0] == 'number':
        return name == 'humn'
    
    _, left, _, right = job
    return contains_humn(left, monkeys) or contains_humn(right, monkeys)


def solve_for_humn(name, target, monkeys):
    # Solve backwards: given target value, find what humn should be
    if name == 'humn':
        return target
    
    job = monkeys[name]
    _, left, op, right = job
    
    # Determine which branch contains humn and invert operations
    if contains_humn(left, monkeys):
        right_val = evaluate(right, monkeys)
        if op == '+':
            return solve_for_humn(left, target - right_val, monkeys)
        elif op == '-':
            return solve_for_humn(left, target + right_val, monkeys)
        elif op == '*':
            return solve_for_humn(left, target // right_val, monkeys)
        elif op == '/':
            return solve_for_humn(left, target * right_val, monkeys)
    else:
        left_val = evaluate(left, monkeys)
        if op == '+':
            return solve_for_humn(right, target - left_val, monkeys)
        elif op == '-':
            return solve_for_humn(right, left_val - target, monkeys)
        elif op == '*':
            return solve_for_humn(right, target // left_val, monkeys)
        elif op == '/':
            return solve_for_humn(right, left_val // target, monkeys)


def solve_part_2(lines):
    monkeys = parse_monkeys(lines)
    
    # root is now equality check: find humn value that makes both sides equal
    root_job = monkeys['root']
    left_name = root_job[1]
    right_name = root_job[3]
    
    # Find which side contains humn and solve backwards
    if contains_humn(left_name, monkeys):
        target = evaluate(right_name, monkeys)
        result = solve_for_humn(left_name, target, monkeys)
    else:
        target = evaluate(left_name, monkeys)
        result = solve_for_humn(right_name, target, monkeys)
    
    print(f"Part 2 Solution: {result}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)