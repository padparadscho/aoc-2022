with open('04/input.txt', 'r') as f:
    lines = f.readlines()


def solve_part_1(lines):
    count = 0
    for line in lines:
        line = line.strip()

        if not line:
            continue
        range1, range2 = line.split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))
        
        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            count += 1
        
    print(f"Part 1 Solution: {count}")


def solve_part_2(lines):
    count = 0
    for line in lines:
        line = line.strip()

        if not line:
            continue
        range1, range2 = line.split(',')
        start1, end1 = map(int, range1.split('-'))
        start2, end2 = map(int, range2.split('-'))

        # Ranges overlap if the earlier start is within the later range
        if max(start1, start2) <= min(end1, end2):
            count += 1
    
    print(f"Part 2 Solution: {count}")


if __name__ == '__main__':
    solve_part_1(lines)
    solve_part_2(lines)