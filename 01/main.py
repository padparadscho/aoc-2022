with open('01/input.txt', 'r') as f:
    content = f.read()


def solve_part_1(content):
    # Blank lines separate each elf's inventory
    elves = content.strip().split('\n\n')
    max_calories = max(sum(int(cal) for cal in elf.strip().split('\n') if cal.strip()) for elf in elves)
    print(f"Part 1 Solution: {max_calories}")


def solve_part_2(content):
    elves = content.strip().split('\n\n')
    totals = sorted([sum(int(cal) for cal in elf.strip().split('\n') if cal.strip()) for elf in elves], reverse=True)
    print(f"Part 2 Solution: {sum(totals[:3])}")


if __name__ == "__main__":
    solve_part_1(content)
    solve_part_2(content)