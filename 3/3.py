from lib.lib import read_input_lines
from pprintpp import pprint


board = read_input_lines('in_a.txt')
pprint(board)

# find coordinates of symbols
symbols = {}
for row, line in enumerate(board):
    for column, char in enumerate(line):
        if not char.isnumeric() and not char == '.':
            symbols[row, column] = char

pprint(symbols)

# find numbers

# find numbers associated with symbols without duplicates

# add the numbers
