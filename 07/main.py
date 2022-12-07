with open('07/input.txt') as f:
    lines = f.readlines()


def parse_filesystem(lines):
    path = []  # Current directory path as stack
    dir_sizes = {}  # Maps path tuple to total size
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('$ cd'):
            dirname = line.split()[2]
            if dirname == '/':
                path = []
            elif dirname == '..':
                path.pop()
            else:
                path.append(dirname)
            i += 1
        
        elif line.startswith('$ ls'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('$'):
                parts = lines[i].strip().split()
                if parts[0] != 'dir':  # File with size
                    size = int(parts[0])
                    # Directory size = sum of all files it contains (nested files included)
                    for j in range(len(path) + 1):
                        path_key = tuple(path[:j])
                        dir_sizes[path_key] = dir_sizes.get(path_key, 0) + size
                i += 1
    
    return dir_sizes


def solve_part_1(lines):
    dir_sizes = parse_filesystem(lines)
    total = sum(size for size in dir_sizes.values() if size <= 100000)

    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    dir_sizes = parse_filesystem(lines)
    total_space = 70000000
    needed_space = 30000000
    used_space = dir_sizes[tuple()]  # Root directory
    unused_space = total_space - used_space
    to_free = needed_space - unused_space  # Amount to be freed
    
    candidates = [size for size in dir_sizes.values() if size >= to_free]
    smallest = min(candidates)
    
    print(f"Part 2 Solution: {smallest}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)