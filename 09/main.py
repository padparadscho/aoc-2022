with open('09/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def move_tail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    
    # Already touching (distance <= 1 in both axes)
    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail
    
    # Move tail toward head
    move_x = 0 if dx == 0 else (1 if dx > 0 else -1)
    move_y = 0 if dy == 0 else (1 if dy > 0 else -1)
    return (tail[0] + move_x, tail[1] + move_y)


def simulate_rope(motions, rope_length):
    knots = [(0, 0)] * rope_length
    visited = {(0, 0)}
    
    for line in motions:
        direction, distance = line.split()
        distance = int(distance)
        
        for _ in range(distance):
            # Move head
            if direction == 'L':
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == 'R':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            elif direction == 'U':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            elif direction == 'D':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            
            # Move each knot following the one before it
            for i in range(1, rope_length):
                knots[i] = move_tail(knots[i - 1], knots[i])
            
            visited.add(knots[-1])
    
    return len(visited)


def solve_part_1(lines):
    positions = simulate_rope(lines, 2)

    print(f"Part 1 Solution: {positions}")


def solve_part_2(lines):
    positions = simulate_rope(lines, 10)
    
    print(f"Part 2 Solution: {positions}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)