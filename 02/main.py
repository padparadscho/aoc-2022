with open('02/input.txt', 'r') as f:
    lines = f.readlines()


def solve_part_1(lines):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    outcome_score = {
        ('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
        ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
        ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
    }
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        opponent, me = line.split()
        total += shape_score[me] + outcome_score[(opponent, me)]
    print(f"Part 1 Solution: {total}")


def solve_part_2(lines):
    shape_score = {'X': 1, 'Y': 2, 'Z': 3}
    # X = lose, Y = draw, Z = win
    # For each opponent move and desired outcome, determine the move I need to play
    play = {
        ('A', 'X'): 'Z', ('A', 'Y'): 'X', ('A', 'Z'): 'Y',
        ('B', 'X'): 'X', ('B', 'Y'): 'Y', ('B', 'Z'): 'Z',
        ('C', 'X'): 'Y', ('C', 'Y'): 'Z', ('C', 'Z'): 'X',
    }
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        opponent, result = line.split()
        me = play[(opponent, result)]
        total += shape_score[me] + outcome_score[result]
    print(f"Part 2 Solution: {total}")


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)