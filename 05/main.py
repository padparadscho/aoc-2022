with open('05/input.txt', 'r') as f:
    lines = f.readlines()


def parse_stacks(lines):
    # Find the line with stack numbers
    num_line_idx = None
    for i, line in enumerate(lines):
        if line.strip() and all(c.isdigit() or c.isspace() for c in line):
            num_line_idx = i
            break
    
    # Parse stack configuration from lines above the number line
    num_stacks = len(lines[num_line_idx].split())
    stacks = [[] for _ in range(num_stacks)]
    
    # Parse from bottom to top (reverse order)
    for line in reversed(lines[:num_line_idx]):
        for i in range(num_stacks):
            # Crates are at positions 1, 5, 9, 13, ... (step of 4)
            pos = 1 + i * 4
            if pos < len(line) and line[pos].isalpha():
                stacks[i].append(line[pos])
    
    return stacks


def parse_moves(lines):
    moves = []
    for line in lines:
        if line.startswith('move'):
            parts = line.split()
            count = int(parts[1])
            from_stack = int(parts[3]) - 1
            to_stack = int(parts[5]) - 1
            moves.append((count, from_stack, to_stack))
    return moves


def solve_part_1(lines):
    stacks = parse_stacks(lines)
    moves = parse_moves(lines)
    
    for count, from_stack, to_stack in moves:
        # Crates are moved one at a time (LIFO order)
        for _ in range(count):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    
    result = ''.join(stack[-1] if stack else '' for stack in stacks)
    
    print(f"Part 1 Solution: {result}")


def solve_part_2(lines):
    stacks = parse_stacks(lines)
    moves = parse_moves(lines)
    
    for count, from_stack, to_stack in moves:
        # Crates are moved all at once (preserving order)
        crates = stacks[from_stack][-count:]
        stacks[from_stack] = stacks[from_stack][:-count]
        stacks[to_stack].extend(crates)
    
    result = ''.join(stack[-1] if stack else '' for stack in stacks)

    print(f"Part 2 Solution: {result}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)