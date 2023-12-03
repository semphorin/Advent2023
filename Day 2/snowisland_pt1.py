import re

data = open('data.txt', 'r')
lines = data.readlines()

rg = re.compile(r'[0-9]+ red')
bg = re.compile(r'[0-9]+ blue')
gg = re.compile(r'[0-9]+ green')
game_num = re.compile(r'[0-9]+')
game_num_sum = 0

for line in lines:
    r,b,g = 0,0,0
    matches = rg.findall(line)
    for match in matches:
        if int(match[0] + match[1]) > r:
            r = int(match[0] + match[1])
    matches = bg.findall(line)
    for match in matches:
        if int(match[0] + match[1]) > b:
            b = int(match[0] + match[1])
    matches = gg.findall(line)
    for match in matches:
        if int(match[0] + match[1]) > g:
            g = int(match[0] + match[1])
    
    game = game_num.findall(line)
    if r <= 12 and g <= 13 and b <= 14:
        game_num_sum += int(game[0])
        print(f'Game is possible! game num = {game[0]}, current sum = {game_num_sum}')
    
    print('threshold:')
    print('r=12, g=13, b=14')
    print(f'r={r}, g={g}, b={b}\n')
    
print(game_num_sum)