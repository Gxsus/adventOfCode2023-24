#Part one
ris = 0
with open('input.txt', 'r') as file:
    for i in range(1, 101):
        check = True
        game = file.readline().replace(f'Game {i}: ', '').strip().split('; ')
        for st in game:  # st stands for set, which is a keyword
            for cubes in st.split(', '):
                tmp = cubes.split()
                if 'red' == tmp[1] and int(tmp[0]) > 12:
                    check = False
                if 'green' == tmp[1] and int(tmp[0]) > 13:
                    check = False
                if 'blue' == tmp[1] and int(tmp[0]) > 14:
                    check = False
        if check:
            ris += i
print(ris)

#Part two
ris = 0
with open('input.txt', 'r') as file:
    for i in range(1, 101):
        c = {'red': 0, 'green': 0, 'blue': 0}
        game = file.readline().replace(f'Game {i}: ', '').strip().split('; ')
        for st in game:  # st stands for set, which is a keyword
            for cubes in st.split(', '):
                tmp = cubes.split()
                if c[tmp[1]] < int(tmp[0]):
                    c[tmp[1]] = int(tmp[0])
        ris += (c['red'] * c['green'] * c['blue'])
print(ris)
