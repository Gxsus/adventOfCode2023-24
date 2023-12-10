#Part one
ris = 0
def getSurrounders(x,y, x_max, y_max):
    ret = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if 0 <= i < y_max and 0 <= j < x_max and (i != y or j != x):
                ret.append([j, i])  # x, y
    return ret


with open('input.txt', 'r') as file:
    engine = file.read().split('\n')
    x_max, y_max = len(engine[0]), len(engine)
    for i in range(y_max):
        for j in range(x_max):
            if not(ord('0') <= ord(engine[i][j]) <= ord('9')) and engine[i][j] != '.':
                surrounders = getSurrounders(j, i, x_max, y_max)
                for x, y in surrounders:
                    number = ''
                    if ord('0') <= ord(engine[y][x]) <= ord('9'):
                        number = engine[y][x]
                        engine[y] = engine[y][:x] + '.' + engine[y][x + 1:]
                        for tmp_x in range(x - 1, -1, -1):
                            if not(ord('0') <= ord(engine[y][tmp_x]) <= ord('9')):
                                break
                            number = engine[y][tmp_x] + number
                            engine[y] = engine[y][:tmp_x] + '.' + engine[y][tmp_x + 1:]
                        for tmp_x in range(x + 1, x_max):
                            if not(ord('0') <= ord(engine[y][tmp_x]) <= ord('9')):
                                break
                            number += engine[y][tmp_x]
                            engine[y] = engine[y][:tmp_x] + '.' + engine[y][tmp_x + 1:]
                        ris += int(number)
print(ris)

#Part two
ris = 0
def getSurrounders(x,y, x_max, y_max):
    ret = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if 0 <= i < y_max and 0 <= j < x_max and (i != y or j != x):
                ret.append([j, i])  # x, y
    return ret


with open('input.txt', 'r') as file:
    engine = file.read().split('\n')
    x_max, y_max = len(engine[0]), len(engine)
    for i in range(y_max):
        for j in range(x_max):
            if engine[i][j] == '*':
                numbers = []
                surrounders = getSurrounders(j, i, x_max, y_max)
                for x, y in surrounders:
                    if ord('0') <= ord(engine[y][x]) <= ord('9'):
                        number = engine[y][x]
                        engine[y] = engine[y][:x] + '.' + engine[y][x + 1:]
                        for tmp_x in range(x - 1, -1, -1):
                            if not(ord('0') <= ord(engine[y][tmp_x]) <= ord('9')):
                                break
                            number = engine[y][tmp_x] + number
                            engine[y] = engine[y][:tmp_x] + '.' + engine[y][tmp_x + 1:]
                        for tmp_x in range(x + 1, x_max):
                            if not(ord('0') <= ord(engine[y][tmp_x]) <= ord('9')):
                                break
                            number += engine[y][tmp_x]
                            engine[y] = engine[y][:tmp_x] + '.' + engine[y][tmp_x + 1:]
                        numbers.append(number)
                if len(numbers) == 2:
                    ris += (int(numbers[0]) * int(numbers[1]))
print(ris)
