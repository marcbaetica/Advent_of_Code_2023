from lib.lib import read_input_lines


max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}
games_played = {}


def extract_game_number(log):
    return int(log.split(':')[0].split(' ')[1])


def extract_game_actions(log):
    return log.split(': ')[1].split('; ')


def extract_champion_from_actions(log):
    red_max = 0
    green_max = 0
    blue_max = 0
    pulls_list = extract_game_actions(log)
    for pull in pulls_list:
        cubes = pull.split(', ')
        for cubes_set in cubes:
            cubes_count, cubes_color = cubes_set.split(' ')
            cubes_count = int(cubes_count)
            red_max = cubes_count if 'red' == cubes_color and cubes_count > red_max else red_max
            green_max = cubes_count if 'green' == cubes_color and cubes_count > green_max else green_max
            blue_max = cubes_count if 'blue' == cubes_color and cubes_count > blue_max else blue_max
    return {'red': red_max, 'green': green_max, 'blue': blue_max}


def solution_a():
    # lines = read_input_lines('in_a.txt')
    lines = read_input_lines('input.txt')
    for line in lines:
        game_number = extract_game_number(line)
        game_champions = extract_champion_from_actions(line)
        games_played[game_number] = game_champions

    score = 0
    for i, cubes_champions in games_played.items():
        colors = ['red', 'green', 'blue']
        if all([cubes_champions[color] <= max_cubes[color] for color in colors]):
            # print(f'Game {i} worked! Champions={cubes_champions}. Expected={max_cubes}.')
            score += i

    print(score)


def solution_b():
    # lines = read_input_lines('in_a.txt')
    lines = read_input_lines('input.txt')
    score = 0
    for line in lines:
        min_set_per_game = extract_champion_from_actions(line)
        power = min_set_per_game['red'] * min_set_per_game['green'] * min_set_per_game['blue']
        score += power
    print(score)


solution_a()
solution_b()
