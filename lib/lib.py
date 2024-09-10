def read_input_lines(file):
    with open(file, 'r') as f:
        return [line.rstrip() for line in f.readlines()]
