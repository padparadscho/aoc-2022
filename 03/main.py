with open('03/input.txt', 'r') as f:
    lines = f.readlines()


def priority(char):
    return ord(char) - ord('a') + 1 if char.islower() else ord(char) - ord('A') + 27


def solve_part_1(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Split line in half: first and second compartments
        mid = len(line) // 2
        first, second = set(line[:mid]), set(line[mid:])
        common = (first & second).pop()
        total += priority(common)
    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    total = 0
    # Groups of 3 lines represent one elf group
    for i in range(0, len(lines), 3):
        group = [set(line.strip()) for line in lines[i:i+3] if line.strip()]
        if len(group) == 3:
            common = (group[0] & group[1] & group[2]).pop()
            total += priority(common)
    print(f"Part 2 Solution: {total}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)