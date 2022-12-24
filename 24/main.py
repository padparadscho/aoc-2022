from collections import deque
from math import lcm

with open('24/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_input(lines):
    height = len(lines)
    width = len(lines[0])
    
    blizzards = []
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            char = lines[row][col]
            if char in '^v<>':
                blizzards.append((row, col, char))
    
    # Start is always at top row, column 1
    start = (0, 1)
    # End is always at bottom row, column width-2
    end = (height - 1, width - 2)
    
    return blizzards, start, end, height, width


def precompute_blizzards(blizzards, height, width, period):
    # Precompute blizzard positions for each time step
    # Period is LCM of (height-2) and (width-2) since blizzards wrap
    positions = []
    for t in range(period):
        pos = set()
        for row, col, direction in blizzards:
            if direction == '^':
                new_row = 1 + (row - 1 - t) % (height - 2)
                new_col = col
            elif direction == 'v':
                new_row = 1 + (row - 1 + t) % (height - 2)
                new_col = col
            elif direction == '<':
                new_row = row
                new_col = 1 + (col - 1 - t) % (width - 2)
            else:  # '>'
                new_row = row
                new_col = 1 + (col - 1 + t) % (width - 2)
            pos.add((new_row, new_col))
        positions.append(pos)
    return positions


def bfs(start, end, start_time, blizzard_positions, height, width, period):
    # BFS with periodic state: (row, col, time % period)
    queue = deque([(start[0], start[1], start_time)])
    visited = set()
    visited.add((start[0], start[1], start_time % period))
    
    while queue:
        row, col, time = queue.popleft()
        
        if (row, col) == end:
            return time
        
        next_time = time + 1
        blizzards = blizzard_positions[next_time % period]
        
        # Try all 5 moves: up, down, left, right, wait
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]:
            new_row = row + dr
            new_col = col + dc
            
            # Check bounds
            if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                continue
            
            # Check walls
            if lines[new_row][new_col] == '#':
                continue
            
            # Check blizzards
            if (new_row, new_col) in blizzards:
                continue
            
            # Check visited with periodic state
            state = (new_row, new_col, next_time % period)
            if state in visited:
                continue
            
            visited.add(state)
            queue.append((new_row, new_col, next_time))
    
    return -1


def solve_part_1(lines):
    blizzards, start, end, height, width = parse_input(lines)
    period = lcm(height - 2, width - 2)
    blizzard_positions = precompute_blizzards(blizzards, height, width, period)
    
    time = bfs(start, end, 0, blizzard_positions, height, width, period)

    print(f"Part 1 Solution: {time}")


def solve_part_2(lines):
    blizzards, start, end, height, width = parse_input(lines)
    period = lcm(height - 2, width - 2)
    blizzard_positions = precompute_blizzards(blizzards, height, width, period)
    
    # Three trips: start -> end -> start -> end
    time1 = bfs(start, end, 0, blizzard_positions, height, width, period)
    time2 = bfs(end, start, time1, blizzard_positions, height, width, period)
    time3 = bfs(start, end, time2, blizzard_positions, height, width, period)
    
    print(f"Part 2 Solution: {time3}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)