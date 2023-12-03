# Description: Day 3 of Advent of Code
# Part 1:
import copy

with open('data.txt') as f:
    parts = []
    symbols = []
    numbers = []
    for line in f.readlines():
        part = []
        symbol = []
        number = []
        line = line.strip()
        for i in range(len(line)):
            part.append(line[i])
            if line[i].isdigit():
                number.append(line[i])
            else:
                number.append(None)
            if (line[i] != '.') and (not line[i].isdigit()):
                symbol.append(True)
            else:
                symbol.append(False)
        symbols.append(symbol)
        numbers.append(number)
        parts.append(part)
    new_symbols = copy.deepcopy(symbols)

    for i in range(len(symbols)):
        for j in range(len(symbols[0])):
            if symbols[i][j]:
                new_symbols[i-1][j-1] = True
                new_symbols[i-1][j] = True
                new_symbols[i-1][j+1] = True
                new_symbols[i][j-1] = True
                new_symbols[i][j+1] = True
                new_symbols[i+1][j-1] = True
                new_symbols[i+1][j] = True
                new_symbols[i+1][j+1] = True

    sum = 0
    for i in range(len(parts)):
        j = 0
        while j < len(parts[i]):
            if parts[i][j].isdigit():
                k = j + 1
                num = str(parts[i][j])
                is_counted = new_symbols[i][j]
                while (k < len(parts[i])) and parts[i][k].isdigit():
                    if new_symbols[i][k]:
                            is_counted = True
                    num = num + str(parts[i][k])
                    k += 1
                if is_counted:
                    sum += int(num)
                j = k
            else:
                j += 1
    print(sum)
