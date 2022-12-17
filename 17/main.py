with open('17/input.txt') as f:
    jets = f.read().strip()


# Rock shapes defined as lists of (row, col) offsets from bottom-left
ROCKS = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # Horizontal line
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # Plus
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # L-shape
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # Vertical line
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # Square
]


def solve_part_1(jets):
    occupied = set()
    jet_idx = 0
    height = 0
    
    for rock_num in range(2022):
        rock_type = rock_num % 5
        rock = ROCKS[rock_type]
        
        # Spawn 3 units above current height
        spawn_row = height + 3
        spawn_col = 2
        rock_positions = [(spawn_row + dr, spawn_col + dc) for dr, dc in rock]
        
        while True:
            # Jet push
            jet = jets[jet_idx]
            jet_idx = (jet_idx + 1) % len(jets)
            
            if jet == '<':
                new_positions = [(r, c - 1) for r, c in rock_positions]
                if all(c >= 0 and (r, c) not in occupied for r, c in new_positions):
                    rock_positions = new_positions
            else:
                new_positions = [(r, c + 1) for r, c in rock_positions]
                if all(c < 7 and (r, c) not in occupied for r, c in new_positions):
                    rock_positions = new_positions
            
            # Gravity
            new_positions = [(r - 1, c) for r, c in rock_positions]
            if any(r < 0 or (r, c) in occupied for r, c in new_positions):
                occupied.update(rock_positions)
                height = max(height, max(r for r, c in rock_positions) + 1)
                break
            else:
                rock_positions = new_positions
    
    print(f"Part 1 Solution: {height}")


def solve_part_2(jets):
    # Track columns instead of positions for efficiency
    columns = [set() for _ in range(7)]  # Track occupied rows per column
    jet_idx = 0
    height = 0
    
    # Dictionary for cycle detection
    fingerprints = {}
    
    target = 1000000000000
    done_at = None
    done_at_val = None
    done_at_height = None
    
    rock_num = 0
    while rock_num < target:
        rock_type = rock_num % 5
        rock = ROCKS[rock_type]
        
        # Create fingerprint: rock type, jet index, and relative column heights
        max_heights = tuple(max(col) if col else 0 for col in columns)
        fingerprint = (rock_type, jet_idx, tuple(h - height + 1000 for h in max_heights))
        
        if fingerprint in fingerprints:
            start_rock, start_height = fingerprints[fingerprint]
            period = rock_num - start_rock
            remaining = target - start_rock
            num_cycles = remaining // period
            done_at = rock_num + remaining % period
            done_at_val = start_height + num_cycles * (height - start_height)
            done_at_height = height
        
        if done_at is not None and rock_num == done_at:
            result = done_at_val + (height - done_at_height)
            print(f"Part 2 Solution: {result}")
            return
        
        fingerprints[fingerprint] = (rock_num, height)
        
        # Spawn rock
        spawn_row = height + 3
        spawn_col = 2
        rock_positions = [(spawn_row + dr, spawn_col + dc) for dr, dc in rock]
        
        while True:
            jet = jets[jet_idx]
            jet_idx = (jet_idx + 1) % len(jets)
            
            if jet == '<':
                new_positions = [(r, c - 1) for r, c in rock_positions]
                if all(c >= 0 and r not in columns[c] for r, c in new_positions):
                    rock_positions = new_positions
            else:
                new_positions = [(r, c + 1) for r, c in rock_positions]
                if all(c < 7 and r not in columns[c] for r, c in new_positions):
                    rock_positions = new_positions
            
            new_positions = [(r - 1, c) for r, c in rock_positions]
            if any(r < 0 or r in columns[c] for r, c in new_positions):
                for r, c in rock_positions:
                    columns[c].add(r)
                height = max(height, max(r for r, c in rock_positions) + 1)
                break
            else:
                rock_positions = new_positions
        
        rock_num += 1


if __name__ == '__main__':
    solve_part_1(jets)
    solve_part_2(jets)