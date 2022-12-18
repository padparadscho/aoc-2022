with open('18/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_cubes(lines):
    cubes = set()
    for line in lines:
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))
    return cubes


def solve_part_1(lines):
    cubes = parse_cubes(lines)
    
    # Count exposed faces: each cube has 6 faces minus adjacent cubes
    surface_area = 0
    for x, y, z in cubes:
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) not in cubes:
                surface_area += 1
    
    print(f"Part 1 Solution: {surface_area}")


def solve_part_2(lines):
    cubes = parse_cubes(lines)
    
    # Find bounding box
    min_x = min(x for x, y, z in cubes)
    max_x = max(x for x, y, z in cubes)
    min_y = min(y for x, y, z in cubes)
    max_y = max(y for x, y, z in cubes)
    min_z = min(z for x, y, z in cubes)
    max_z = max(z for x, y, z in cubes)
    
    # Flood fill from outside to find exterior air (outside the lava droplet)
    exterior_air = set()
    queue = [(min_x - 1, min_y - 1, min_z - 1)]
    exterior_air.add(queue[0])
    
    while queue:
        x, y, z = queue.pop(0)
        
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            # Check if inside bounding box (with margin for exterior)
            if min_x - 1 <= nx <= max_x + 1 and min_y - 1 <= ny <= max_y + 1 and min_z - 1 <= nz <= max_z + 1:
                if (nx, ny, nz) not in cubes and (nx, ny, nz) not in exterior_air:
                    exterior_air.add((nx, ny, nz))
                    queue.append((nx, ny, nz))
    
    # Count faces adjacent to exterior air
    exterior_surface_area = 0
    for x, y, z in cubes:
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) in exterior_air:
                exterior_surface_area += 1
    
    print(f"Part 2 Solution: {exterior_surface_area}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)