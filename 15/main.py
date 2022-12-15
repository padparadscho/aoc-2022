import re


with open('15/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_input(lines):
    sensors = []
    for line in lines:
        match = re.search(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
        if match:
            sx, sy, bx, by = map(int, match.groups())
            dist = abs(sx - bx) + abs(sy - by)
            sensors.append((sx, sy, bx, by, dist))
    return sensors


def solve_part_1(lines):
    sensors = parse_input(lines)
    target_y = 2000000
    
    # Find all x positions where beacons cannot exist in the target row
    impossible = set()
    beacons_in_row = set()
    
    for sx, sy, bx, by, dist in sensors:
        # Manhattan distance: |x - sx| + |y - sy| <= dist
        # For target_y: |x - sx| <= dist - |target_y - sy|
        dy = abs(target_y - sy)
        if dy <= dist:
            # x range: sx - (dist - dy) to sx + (dist - dy)
            dx_max = dist - dy
            for x in range(sx - dx_max, sx + dx_max + 1):
                impossible.add(x)
        
        if by == target_y:
            beacons_in_row.add(bx)
    
    # Remove positions where beacons actually exist
    count = len(impossible) - len(beacons_in_row)
    
    print(f"Part 1 Solution: {count}")


def solve_part_2(lines):
    sensors = parse_input(lines)
    max_coord = 4000000
    
    # Check boundaries of sensor ranges
    for sx, sy, bx, by, dist in sensors:
        # Beacon must be exactly dist+1 away from sensor
        # Check all positions on the boundary
        for dx in range(dist + 2):
            dy = dist + 1 - dx
            
            for x, y in [(sx + dx, sy + dy), (sx + dx, sy - dy),
                          (sx - dx, sy + dy), (sx - dx, sy - dy)]:
                if 0 <= x <= max_coord and 0 <= y <= max_coord:
                    # Check if this position is outside all sensor ranges
                    valid = True
                    for sx2, sy2, bx2, by2, dist2 in sensors:
                        if abs(x - sx2) + abs(y - sy2) <= dist2:
                            valid = False
                            break
                    
                    if valid:
                        frequency = x * 4000000 + y
                        print(f"Part 2 Solution: {frequency}")
                        return


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)