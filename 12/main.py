with open('12/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_grid(lines):
    # Elevation: S=0, E=25, a-z=0-25
    grid = []
    start = None
    end = None
    for row, line in enumerate(lines):
        grid_row = []
        for col, char in enumerate(line):
            if char == 'S':
                start = (row, col)
                grid_row.append(0)
            elif char == 'E':
                end = (row, col)
                grid_row.append(25)
            else:
                grid_row.append(ord(char) - ord('a'))
        grid.append(grid_row)
    return grid, start, end


def bfs_shortest_path(grid, start, is_goal, can_move):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    queue = [(start[0], start[1], 0)]
    visited.add(start)
    
    while queue:
        row, col, steps = queue.pop(0)
        
        if is_goal(row, col):
            return steps
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if (new_row, new_col) not in visited:
                    if can_move(row, col, new_row, new_col):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col, steps + 1))
    
    return float('inf')


def solve_part_1(lines):
    grid, start, end = parse_grid(lines)
    
    def is_goal(row, col):
        return (row, col) == end
    
    # Can climb at most +1 elevation level
    def can_move(row, col, new_row, new_col):
        return grid[new_row][new_col] <= grid[row][col] + 1
    
    steps = bfs_shortest_path(grid, start, is_goal, can_move)
    
    print(f"Part 1 Solution: {steps}")


def solve_part_2(lines):
    grid, _, end = parse_grid(lines)
    
    # Reverse: start from E, find shortest path to any 'a' (elevation 0)
    def is_goal(row, col):
        return grid[row][col] == 0
    
    # Reverse movement: can descend any height, but only climb +1
    def can_move(row, col, new_row, new_col):
        return grid[row][col] <= grid[new_row][new_col] + 1
    
    steps = bfs_shortest_path(grid, end, is_goal, can_move)

    print(f"Part 2 Solution: {steps}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)