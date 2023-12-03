with open("input2.txt") as f:
    data = f.read().splitlines()

target_sum = {
    'red': 12,
    'blue': 14,
    'green': 13
}

get_sum = 0

for line in data:
    split_game = line.split(':')
    id_game = split_game[0].split(' ')[1]
    cube_set = split_game[1]
    subsets = cube_set.split(';')
    possible_sum = True
    min_target_sum = {'red': 0, 'blue': 0, 'green': 0}
    for game_set in subsets:
        color = game_set.split(',')
        for draw in color:
            count = draw.split(' ')[0]
            color_info = draw.split(' ')[1]
            min_target_sum[color_info] = max(min_target_sum[color_info], int(count))
        total = 1
        for k, v in min_target_sum.items():
            total *= v
            get_sum += total
print(get_sum)
