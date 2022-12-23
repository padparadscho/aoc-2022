with open('23/input.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]


# Direction order: N, S, W, E
DIRECTIONS = [
    (-1, 0, [(-1, -1), (-1, 0), (-1, 1)]),  # N: check NW, N, NE
    (1, 0, [(1, -1), (1, 0), (1, 1)]),      # S: check SW, S, SE
    (0, -1, [(-1, -1), (0, -1), (1, -1)]),  # W: check NW, W, SW
    (0, 1, [(-1, 1), (0, 1), (1, 1)])       # E: check NE, E, SE
]


def parse_elves(lines):
    elves = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                elves.add((row, col))
    return elves


def count_adjacent_elves(elves, pos):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if (pos[0] + dr, pos[1] + dc) in elves:
                count += 1
    return count


def simulate_round(elves, directions):
    proposals = {}
    proposal_counts = {}
    
    for elf in elves:
        if count_adjacent_elves(elves, elf) == 0:
            continue
        
        for direction, (_, _, checks) in enumerate(directions):
            # Check if all 3 adjacent cells in direction are empty
            can_move = all((elf[0] + dr, elf[1] + dc) not in elves for dr, dc in checks)
            
            if can_move:
                new_pos = (elf[0] + directions[direction][0], elf[1] + directions[direction][1])
                proposals[elf] = new_pos
                proposal_counts[new_pos] = proposal_counts.get(new_pos, 0) + 1
                break
    
    moved = False
    for elf, new_pos in proposals.items():
        if proposal_counts[new_pos] == 1:
            elves.remove(elf)
            elves.add(new_pos)
            moved = True
    
    directions.append(directions.pop(0))
    return moved


def solve_part_1(lines):
    elves = parse_elves(lines)
    directions = DIRECTIONS.copy()
    
    for _ in range(10):
        simulate_round(elves, directions)
    
    # Calculate empty ground
    min_row = min(elf[0] for elf in elves)
    max_row = max(elf[0] for elf in elves)
    min_col = min(elf[1] for elf in elves)
    max_col = max(elf[1] for elf in elves)
    
    total_tiles = (max_row - min_row + 1) * (max_col - min_col + 1)
    empty_tiles = total_tiles - len(elves)
    
    print(f"Part 1 Solution: {empty_tiles}")


def solve_part_2(lines):
    elves = parse_elves(lines)
    directions = DIRECTIONS.copy()
    
    round_num = 0
    while True:
        round_num += 1
        if not simulate_round(elves, directions):
            break
    
    print(f"Part 2 Solution: {round_num}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)