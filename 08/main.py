with open('08/input.txt') as f:
    lines = f.readlines()


def parse_grid(lines):
    return [[int(c) for c in line.strip()] for line in lines]


def is_visible(grid, row, col):
    height = grid[row][col]
    rows = len(grid)
    cols = len(grid[0])
    
    # Edge trees are always visible
    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
        return True
    
    # Check visibility from each edge direction
    up = all(grid[r][col] < height for r in range(row - 1, -1, -1))
    down = all(grid[r][col] < height for r in range(row + 1, rows))
    left = all(grid[row][c] < height for c in range(col - 1, -1, -1))
    right = all(grid[row][c] < height for c in range(col + 1, cols))
    
    return up or down or left or right


def solve_part_1(lines):
    grid = parse_grid(lines)
    rows = len(grid)
    cols = len(grid[0])
    
    visible_count = 0
    for row in range(rows):
        for col in range(cols):
            if is_visible(grid, row, col):
                visible_count += 1
    
    print(f"Part 1 Solution: {visible_count}")


def viewing_distance(grid, row, col, dr, dc):
    height = grid[row][col]
    rows = len(grid)
    cols = len(grid[0])
    
    r, c = row + dr, col + dc
    distance = 0
    
    # Count trees until edge or blocking tree (>=height)
    while 0 <= r < rows and 0 <= c < cols:
        distance += 1
        if grid[r][c] >= height:
            break
        r += dr
        c += dc
    
    return distance


def scenic_score(grid, row, col):
    # Scenic score: product of viewing distances in 4 directions
    up = viewing_distance(grid, row, col, -1, 0)
    down = viewing_distance(grid, row, col, 1, 0)
    left = viewing_distance(grid, row, col, 0, -1)
    right = viewing_distance(grid, row, col, 0, 1)
    
    return up * down * left * right


def solve_part_2(lines):
    grid = parse_grid(lines)
    rows = len(grid)
    cols = len(grid[0])
    
    max_score = 0
    for row in range(rows):
        for col in range(cols):
            score = scenic_score(grid, row, col)
            max_score = max(max_score, score)
    
    print(f"Part 2 Solution: {max_score}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)