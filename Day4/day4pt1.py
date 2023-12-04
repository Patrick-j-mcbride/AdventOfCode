
def extract_line(line):
    data = {'id': 0, 'winners': [], 'numbers': [], 'points': 0}
    line = line.split(':')
    data['id'] = int(''.join(filter(str.isdigit, line[0])))
    line = line[1].split('|')
    win = line[0].split(' ')
    num = line[1].split(' ')
    for i in range(len(win)):
        if win[i] != '':
            data['winners'].append(int(win[i]))
    for i in range(len(num)):
        if num[i] != '':
            data['numbers'].append(int(num[i]))
    
    return data

total = 0

with open('data.txt') as f:
    cards = []
    for line in f.readlines():
        line = line.strip()
        cards.append(extract_line(line))

    for card in cards:
        for number in card['numbers']:
            if number in card['winners']:
                if card['points'] == 0:
                    card['points'] = 1
                else:
                    card['points'] = card['points'] * 2
    
    for card in cards:
        total += card['points']
    
    print(total)

