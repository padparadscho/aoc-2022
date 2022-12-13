from functools import cmp_to_key


with open('13/input.txt') as f:
    content =f.read()


def compare(left, right):
    # Returns: -1 (correct order), 1 (incorrect order), 0 (equal)
    # Both integers: compare values
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    
    # Mixed types: convert integer to list
    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    
    # Both lists: compare element by element
    for i in range(min(len(left), len(right))):
        result = compare(left[i], right[i])
        if result != 0:
            return result
    
    # List length determines order
    if len(left) < len(right):
        return -1
    elif len(left) > len(right):
        return 1
    else:
        return 0


def solve_part_1(content):
    pairs = content.strip().split('\n\n')
    correct_indices = []
    
    for idx, pair in enumerate(pairs, 1):
        left, right = pair.split('\n')
        left = eval(left)
        right = eval(right)
        
        if compare(left, right) == -1:
            correct_indices.append(idx)
    
    result = sum(correct_indices)

    print(f"Part 1 Solution: {result}")


def solve_part_2(content):
    divider1 = [[2]]
    divider2 = [[6]]
    
    # Parse all packets
    packets = [eval(line) for line in content.strip().split('\n') if line]
    packets.extend([divider1, divider2])
    
    # Sort using comparison function
    packets.sort(key=cmp_to_key(compare))
    
    # Find divider indices (1-indexed)
    idx1 = packets.index(divider1) + 1
    idx2 = packets.index(divider2) + 1
    
    result = idx1 * idx2
    
    print(f"Part 2 Solution: {result}")


if __name__ == '__main__':
    solve_part_1(content)
    solve_part_2(content)