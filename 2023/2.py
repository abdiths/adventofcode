from collections import defaultdict

with open("input2.txt") as f:
    input_data = f.read().strip()

part1_total = 0
part2_total = 0

MAX_COUNTS = {'red': 12, 'green': 13, 'blue': 14}

for game in input_data.split("\n"):
    valid = True
    game_id, cube_str = game.split(":")
    cube_counts = defaultdict(int)
    
    for cube_set in cube_str.split(";"):
        for cube in cube_set.split(","):
            num, color = cube.split() 
            num = int(num)
            
            cube_counts[color] = max(cube_counts[color], num)
            
            if num > MAX_COUNTS[color]:
                valid = False
                
    if valid:
        part1_total += int(game_id.split()[-1])
        part2_score = 1
        for count in cube_counts.values():
            part2_score *= count
        part2_total += part2_score
        
print(part1_total, part2_total)