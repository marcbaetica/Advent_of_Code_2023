import re
from lib.lib import read_input_lines
from pprintpp import pprint


schematic = read_input_lines('in_a.txt')
pprint(schematic)


# find coordinates of symbols
symbols = {(r, c): [] for r in range(len(schematic)) for c in range(len(schematic[r])) if schematic[r][c] not in '0123456789.'}
pprint(symbols)

# find all numbers

# pprint(matches)


# find numbers associated with symbols without duplicates
symbol_boundaries = {(r, c): {(r-1, r, r+1), (c-1, c, c+1)} for r, c in symbols.keys()}
pprint(symbol_boundaries)
# add the numbers
