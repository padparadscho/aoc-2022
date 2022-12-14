with open('14/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_rocks(lines):
    rocks = set()
    for line in lines:
        points = []
        for coord in line.split(' -> '):
            x, y = map(int, coord.split(','))
            points.append((x, y))
        
        # Draw lines between consecutive points
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.add((x, y1))
    
    return rocks


def drop_sand(rocks, sand, max_y, has_floor):
    x, y = 500, 0
    
    # Check if source is blocked
    if (x, y) in sand or (x, y) in rocks:
        return None
    
    while y < max_y + 100:  # Limit iterations for safety
        if (x, y + 1) not in rocks and (x, y + 1) not in sand:
            y += 1
        elif (x - 1, y + 1) not in rocks and (x - 1, y + 1) not in sand:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in rocks and (x + 1, y + 1) not in sand:
            x += 1
            y += 1
        else:
            return (x, y)
        
        # Without floor: fell into void
        if not has_floor and y > max_y:
            return None
    
    return None


def solve_part_1(lines):
    rocks = parse_rocks(lines)
    max_y = max(y for _, y in rocks)
    
    sand = set()
    count = 0
    
    while True:
        result = drop_sand(rocks, sand, max_y, has_floor=False)
        if result is None:
            break
        sand.add(result)
        count += 1
    
    print(f"Part 1 Solution: {count}")


def solve_part_2(lines):
    rocks = parse_rocks(lines)
    max_y = max(y for _, y in rocks)
    floor_y = max_y + 2
    
    # Add floor as rocks
    for x in range(500 - floor_y - 10, 500 + floor_y + 10):
        rocks.add((x, floor_y))
    
    sand = set()
    count = 0
    
    while True:
        result = drop_sand(rocks, sand, max_y + 2, has_floor=True)
        if result is None:
            break
        sand.add(result)
        count += 1
    
    print(f"Part 2 Solution: {count}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)