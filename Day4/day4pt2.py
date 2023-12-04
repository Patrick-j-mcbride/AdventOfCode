import copy


def extract_line(line):
    data = {'id': 0, 'winners': [], 'numbers': [], 'points': 1}
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

def process_cards(cards):
    i = 0
    total = 0
    while i < len(cards):
        ct = 0
        for number in cards[i]['numbers']:
            if number in cards[i]['winners']:
                ct += 1
        if ct > 0:
            for h in range(cards[i]['points']):
                for j in range(ct):
                    cards[i+j+1]['points'] = cards[i+j+1]['points'] + 1
        i += 1

    for c in cards:
        total += c['points']
    
    return total

total = 0

with open('data.txt') as f:
    cards = []
    for line in f.readlines():
        line = line.strip()
        cards.append(extract_line(line))

    print(process_cards(cards))