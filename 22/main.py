with open('22/input.txt') as f:
    lines = f.read().split('\n')


def parse_input(lines):
    blank_idx = lines.index('')
    grid = {}
    
    for row, line in enumerate(lines[:blank_idx]):
        for col, char in enumerate(line):
            if char in '.#':
                grid[(row, col)] = char
    
    instructions = lines[blank_idx + 1]
    return grid, instructions


def parse_instructions(instructions):
    result = []
    i = 0
    while i < len(instructions):
        if instructions[i] in 'LR':
            result.append(instructions[i])
            i += 1
        else:
            j = i
            while j < len(instructions) and instructions[j].isdigit():
                j += 1
            result.append(int(instructions[i:j]))
            i = j
    return result


def solve_part_1(lines):
    grid, instructions = parse_input(lines)
    moves = parse_instructions(instructions)
    
    row = 0
    col = min(c for (r, c) in grid if r == 0)  # Start at leftmost valid column
    facing = 0
    # Right, down, left, up
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for move in moves:
        if move == 'L':
            facing = (facing - 1) % 4
        elif move == 'R':
            facing = (facing + 1) % 4
        else:
            for _ in range(move):
                dr, dc = dirs[facing]
                nr, nc = row + dr, col + dc
                
                # Wrap around edges
                if (nr, nc) not in grid:
                    if facing == 0:
                        nc = min(c for (r, c) in grid if r == row)
                    elif facing == 1:
                        nr = min(r for (r, c) in grid if c == col)
                    elif facing == 2:
                        nc = max(c for (r, c) in grid if r == row)
                    else:
                        nr = max(r for (r, c) in grid if c == col)
                
                if grid[(nr, nc)] == '#':
                    break
                row, col = nr, nc
    
    password = 1000 * (row + 1) + 4 * (col + 1) + facing
    
    print(f"Part 1 Solution: {password}")


def solve_part_2(lines):
    grid, instructions = parse_input(lines)
    moves = parse_instructions(instructions)
    
    row = 0
    col = min(c for (r, c) in grid if r == 0)
    dr, dc = 0, 1  # Start facing right
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for move in moves:
        if move == 'L':
            dr, dc = -dc, dr  # Rotate left
        elif move == 'R':
            dr, dc = dc, -dr  # Rotate right
        else:
            for _ in range(move):
                nr, nc = row + dr, col + dc
                cdr, cdc = dr, dc
                
                # Folded cube: hardcoded edge transitions for 50x50 faces
                if nr < 0 and 50 <= nc < 100 and dr == -1:
                    dr, dc = 0, 1
                    nr, nc = nc + 100, 0
                elif nc < 0 and 150 <= nr < 200 and dc == -1:
                    dr, dc = 1, 0
                    nr, nc = 0, nr - 100
                elif nr < 0 and 100 <= nc < 150 and dr == -1:
                    nr, nc = 199, nc - 100
                elif nr >= 200 and 0 <= nc < 50 and dr == 1:
                    nr, nc = 0, nc + 100
                elif nc >= 150 and 0 <= nr < 50 and dc == 1:
                    dc = -1
                    nr, nc = 149 - nr, 99
                elif nc == 100 and 100 <= nr < 150 and dc == 1:
                    dc = -1
                    nr, nc = 149 - nr, 149
                elif nr == 50 and 100 <= nc < 150 and dr == 1:
                    dr, dc = 0, -1
                    nr, nc = nc - 50, 99
                elif nc == 100 and 50 <= nr < 100 and dc == 1:
                    dr, dc = -1, 0
                    nr, nc = 49, nr + 50
                elif nr == 150 and 50 <= nc < 100 and dr == 1:
                    dr, dc = 0, -1
                    nr, nc = nc + 100, 49
                elif nc == 50 and 150 <= nr < 200 and dc == 1:
                    dr, dc = -1, 0
                    nr, nc = 149, nr - 100
                elif nr == 99 and 0 <= nc < 50 and dr == -1:
                    dr, dc = 0, 1
                    nr, nc = nc + 50, 50
                elif nc == 49 and 50 <= nr < 100 and dc == -1:
                    dr, dc = 1, 0
                    nr, nc = 100, nr - 50
                elif nc == 49 and 0 <= nr < 50 and dc == -1:
                    dc = 1
                    nr, nc = 149 - nr, 0
                elif nc < 0 and 100 <= nr < 150 and dc == -1:
                    dc = 1
                    nr, nc = 149 - nr, 50
                
                # Hit wall: restore direction and stop
                if grid[(nr, nc)] == '#':
                    dr, dc = cdr, cdc
                    break
                row, col = nr, nc
    
    facing = dirs.index((dr, dc))
    password = 1000 * (row + 1) + 4 * (col + 1) + facing
    
    print(f"Part 2 Solution: {password}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)