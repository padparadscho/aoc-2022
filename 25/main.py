with open('25/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


def snafu_to_decimal(snafu):
    # SNAFU digits: 2=2, 1=1, 0=0, -=-1, ==-2
    result = 0
    for i, char in enumerate(reversed(snafu)):
        if char == '2':
            value = 2
        elif char == '1':
            value = 1
        elif char == '0':
            value = 0
        elif char == '-':
            value = -1
        else:  # char == '='
            value = -2
        result += value * (5 ** i)
    return result


def decimal_to_snafu(decimal):
    if decimal == 0:
        return '0'
    
    result = []
    while decimal > 0:
        remainder = decimal % 5
        decimal //= 5
        
        if remainder == 0:
            result.append('0')
        elif remainder == 1:
            result.append('1')
        elif remainder == 2:
            result.append('2')
        elif remainder == 3:
            result.append('=')
            decimal += 1  # Carry: 3 = 5 - 2, so write '=' (-2) and add 1
        else:  # remainder == 4
            result.append('-')
            decimal += 1  # Carry: 4 = 5 - 1, so write '-' (-1) and add 1
    
    return ''.join(reversed(result))


def solve_part_1(lines):
    total = sum(snafu_to_decimal(line) for line in lines)
    snafu = decimal_to_snafu(total)
    
    print(f"Part 1 Solution: {snafu}")


if __name__ == '__main__':
    solve_part_1(lines)