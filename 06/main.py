with open('06/input.txt') as f:
    lines = f.readlines()


def find_marker(datastream, marker_size):
    for i in range(len(datastream) - marker_size + 1):
        window = datastream[i:i + marker_size]
        if len(set(window)) == marker_size:
            return i + marker_size


def solve_part_1(lines):
    datastream = lines[0].strip()
    # Start-of-packet marker: 4 distinct characters
    result = find_marker(datastream, 4)

    print(f"Part 1 Solution: {result}")


def solve_part_2(lines):
    datastream = lines[0].strip()
    # Start-of-message marker: 14 distinct characters
    result = find_marker(datastream, 14)

    print(f"Part 2 Solution: {result}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)