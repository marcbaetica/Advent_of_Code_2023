from lib.lib import read_input_lines


max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
games = {}


def extract_game_number(log):
    return int(log.split(':')[0].split(' ')[1])


def extract_game_actions(log):
    return log.split(': ')[1].split('; ')


def is_new_val_larger(new_val, champion):
    return new_val > champion


def parse_cube_count(cubes_color):
    (color, count) = cubes_color.split(' ')
    print(color, count)
    return (color, count)


def extract_champion_from_actions(log):
    red_max = 0
    green_max = 0
    blue_max = 0
    pulls_list = extract_game_actions(log)
    for pull in pulls_list:
        cubes = pull.split(', ')
        for cubes_color in cubes:
            red_max = 0 if is_new_val_larger(100, red_max) and parse_cube_count(cubes_color) else red_max
            green_max = 0 if is_new_val_larger(0, green_max) else green_max
            blue_max = 0 if is_new_val_larger(0, blue_max) else blue_max
            # if 'red' in cubes_color:
            #     new_value = int(cubes_color.split(' red')[0])  # TODO: Do this with conditions per color.
            #     red_max = new_value if is_new_val_larger(new_value, red_max) else red_max
            # elif 'green' in cubes_color:
            #     new_value = int(cubes_color.split(' green')[0])  # TODO: Do this with conditions per color.
            #     green_max = new_value if is_new_val_larger(new_value, green_max) else green_max
            # elif 'blue' in cubes_color:
            #     new_value = int(cubes_color.split(' blue')[0])  # TODO: Do this with conditions per color.
            #     blue_max = new_value if is_new_val_larger(new_value, blue_max) else blue_max
    return {'red': red_max, 'green': green_max, 'blue': blue_max}


lines = read_input_lines('in_a.txt')
print(lines)
for line in lines:
    game_number = extract_game_number(line)
    game_champions = extract_champion_from_actions(line)
    games[game_number] = game_champions

print(games)
