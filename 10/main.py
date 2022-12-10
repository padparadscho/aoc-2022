with open('10/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def run_program(lines):
    x = 1
    cycle = 0
    values = []  # X value at each cycle (1-indexed, so index 0 = cycle 1)
    
    for line in lines:
        if line == 'noop':
            cycle += 1
            values.append(x)
        else:  # addx V
            _, v = line.split()
            v = int(v)
            # addx takes 2 cycles: X value doesn't change until after cycle 2
            cycle += 1
            values.append(x)
            cycle += 1
            values.append(x)
            x += v
    
    return values


def solve_part_1(lines):
    values = run_program(lines)
    # Signal strength at cycles 20, 60, 100, 140, 180, 220
    signal_cycles = [20, 60, 100, 140, 180, 220]
    total = 0
    for cycle in signal_cycles:
        # values is 0-indexed, cycle is 1-indexed
        total += cycle * values[cycle - 1]
    
    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    values = run_program(lines)
    # CRT renders letters on 40x6 grid
    
    for row in range(6):
        line = ''
        for col in range(40):
            cycle = row * 40 + col
            x = values[cycle]
            if abs(col - x) <= 1:
                line += '#'
            else:
                line += '.'
        
        print(f"  {line}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)