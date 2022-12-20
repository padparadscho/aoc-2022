with open('20/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def mix(original, current_state):
    # Mix numbers in their original order
    mixed = list(current_state)
    n = len(mixed)
    
    for i in range(n):
        # Find where original index i currently is
        current_pos = mixed.index(original[i])
        value = mixed[current_pos][1]
        
        # Remove from current position
        mixed.pop(current_pos)
        
        # Calculate new position with wrap around
        new_pos = (current_pos + value) % (n - 1)
        mixed.insert(new_pos, original[i])
    
    return mixed


def solve_part_1(lines):
    numbers = [(i, int(line)) for i, line in enumerate(lines)]
    mixed = mix(numbers, numbers)
    
    # Find position of 0
    zero_pos = next(i for i, (_, val) in enumerate(mixed) if val == 0)
    
    # Calculate grove coordinates
    n = len(mixed)
    coord1 = mixed[(zero_pos + 1000) % n][1]
    coord2 = mixed[(zero_pos + 2000) % n][1]
    coord3 = mixed[(zero_pos + 3000) % n][1]
    
    print(f"Part 1 Solution: {coord1 + coord2 + coord3}")


def solve_part_2(lines):
    key = 811589153
    numbers = [(i, int(line) * key) for i, line in enumerate(lines)]
    
    # Mix 10 times, always passing original order
    mixed = list(numbers)
    for _ in range(10):
        mixed = mix(numbers, mixed)
    
    # Find position of 0
    zero_pos = next(i for i, (_, val) in enumerate(mixed) if val == 0)
    
    # Calculate grove coordinates
    n = len(mixed)
    coord1 = mixed[(zero_pos + 1000) % n][1]
    coord2 = mixed[(zero_pos + 2000) % n][1]
    coord3 = mixed[(zero_pos + 3000) % n][1]
    
    print(f"Part 2 Solution: {coord1 + coord2 + coord3}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)