from collections import deque, defaultdict
from functools import lru_cache


with open('16/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def parse_valves(lines):
    valves = {}
    for line in lines:
        parts = line.split('; ')
        valve_part = parts[0]
        tunnel_part = parts[1]
        
        name = valve_part.split()[1]
        flow_rate = int(valve_part.split('=')[1])
        
        if 'tunnels lead to valves' in tunnel_part:
            tunnels = tunnel_part.split('tunnels lead to valves ')[1].split(', ')
        else:
            tunnels = [tunnel_part.split('tunnel leads to valve ')[1]]
        
        valves[name] = (flow_rate, tunnels)
    
    return valves


def compute_distances(valves):
    # BFS to compute shortest distances between all valve pairs
    distances = {}
    for start in valves:
        distances[start] = {start: 0}
        queue = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in valves[current][1]:
                if neighbor not in distances[start]:
                    distances[start][neighbor] = distances[start][current] + 1
                    queue.append(neighbor)
    return distances


def solve_part_1(lines):
    valves = parse_valves(lines)
    distances = compute_distances(valves)
    
    useful_valves = [v for v in valves if valves[v][0] > 0]
    
    # DFS with memoization: find max pressure from current state
    # State: (current_valve, time_remaining, open_valves_bitmask)
    @lru_cache(maxsize=None)
    def max_pressure(current, time, open_bitmask):
        if time <= 0:
            return 0
        
        max_total = 0
        
        if valves[current][0] > 0:
            valve_idx = useful_valves.index(current)
            if not (open_bitmask & (1 << valve_idx)):
                new_open = open_bitmask | (1 << valve_idx)
                pressure_from_valve = valves[current][0] * (time - 1)
                total = pressure_from_valve + max_pressure(current, time - 1, new_open)
                max_total = max(max_total, total)
        
        for next_valve in useful_valves:
            if next_valve == current:
                continue
            dist = distances[current][next_valve]
            if time > dist:
                total = max_pressure(next_valve, time - dist, open_bitmask)
                max_total = max(max_total, total)
        
        return max_total
    
    result = max_pressure('AA', 30, 0)
    print(f"Part 1 Solution: {result}")


def solve_part_2(lines):
    valves = parse_valves(lines)
    distances = compute_distances(valves)
    
    useful_valves = [v for v in valves if valves[v][0] > 0]
    
    # Enumerate all reachable states to find max pressure for each bitmask
    # BFS explores all possible paths, tracking (position, time, open_bitmask)
    visited = {}
    queue = [(('AA', 26, 0), 0)]
    
    while queue:
        (pos, time, open_bitmask), pressure = queue.pop(0)
        
        if time <= 0:
            continue
        
        state = (pos, time, open_bitmask)
        if state in visited and pressure <= visited[state]:
            continue
        visited[state] = pressure
        
        if valves[pos][0] > 0:
            valve_idx = useful_valves.index(pos)
            if not (open_bitmask & (1 << valve_idx)):
                new_open = open_bitmask | (1 << valve_idx)
                new_pressure = pressure + valves[pos][0] * (time - 1)
                queue.append(((pos, time - 1, new_open), new_pressure))
        
        for next_valve in useful_valves:
            if next_valve == pos:
                continue
            dist = distances[pos][next_valve]
            if time > dist:
                queue.append(((next_valve, time - dist, open_bitmask), pressure))
    
    # Group by open_bitmask and find max pressure for each
    best_for_bitmask = defaultdict(int)
    for (pos, time, open_bitmask), pressure in visited.items():
        best_for_bitmask[open_bitmask] = max(best_for_bitmask[open_bitmask], pressure)
    
    # Two agents must open disjoint sets of valves
    max_total = 0
    for mask1, pressure1 in best_for_bitmask.items():
        for mask2, pressure2 in best_for_bitmask.items():
            if mask1 & mask2 == 0:
                max_total = max(max_total, pressure1 + pressure2)
    
    print(f"Part 2 Solution: {max_total}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)