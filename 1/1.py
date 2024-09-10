from lib.lib import read_input_lines


def solution_a():
    # lines = read_input('in_a.txt')
    lines = read_input_lines('input.txt')

    sum = 0
    for line in lines:
        num_chars = [char for char in line if not char.isalpha()]
        sum += int(''.join([num_chars[0], num_chars[-1]]))

    print(sum)


def generate_digits_map():
    alpha_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits_map = dict(zip(alpha_digits, (str(char) for char in range(10))))
    return digits_map


def solution_b():
    # lines = read_input('in_b.txt')
    lines = read_input_lines('input.txt')
    digits_map = generate_digits_map()
    sum = 0

    for line in lines:
        modified_line = []
        for i in range(len(line)):
            if line[i].isnumeric():
                modified_line.append(line[i])
            else:
                for k in digits_map.keys():
                    if line[i:].startswith(k):
                        modified_line.append(digits_map[k])
        sum += int(''.join([modified_line[0], modified_line[-1]]))

    print(sum)


solution_a()
solution_b()
