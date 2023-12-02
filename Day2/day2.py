# Part 1

#Game 1: 20 green, 3 red, 2 blue; 9 red, 16 blue, 18 green; 6 blue, 19 red, 10 green; 12 red, 19 green, 11 blue

def parce_line(line):
    game = {'game_num': 0, 'red': 0, 'blue': 0, 'green': 0}
    line = line.strip()
    line = line.split(':')
    game['game_num'] = int(line[0].strip('Game '))

    line = line[1].strip().split(';')

    for l in line:
        l = l.split(',')
        for i in l:
            i = i.strip(' ')
            if 'red' in i:
                red = int(i.strip(' red'))
                game['red'] = red if red > game['red'] else game['red']
            elif 'blue' in i:
                blue = int(i.strip(' blue'))
                game['blue'] = blue if blue > game['blue'] else game['blue']
            elif 'green' in i:
                green = int(i.strip(' green'))
                game['green'] = green if green > game['green'] else game['green']
    return game

def parce_games(games):
    sum = 0
    for game in games:
        if (game['red'] <= 12) and (game['blue'] <= 14) and (game['green'] <= 13):
            sum += game['game_num']
    return sum


with open('data.txt') as f:
    games = []
    for line in f.readlines():
        games.append(parce_line(line))
    print("Part 1: " ,parce_games(games))
        
# Part 2
    
def cube_power(games):
    sum = 0
    for game in games:
        sum += game['red'] * game['blue'] * game['green']
    return sum


with open('data.txt') as f:
    games = []
    for line in f.readlines():
        games.append(parce_line(line))
    print("Part 2: " ,cube_power(games))