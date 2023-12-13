#Part one
ris = 0
with open('input.txt', 'r') as file:
    for i in range(1, 221):
        numbers = file.readline().strip().replace("Card {:3d}: ".format(i), '').split(' | ')
        winning_numbers = []
        for n in numbers[0].split(' '):
            if n != '':
                winning_numbers.append(n)
        got_numbers = 0
        for n in numbers[1].split(' '):
            if n in winning_numbers:
                got_numbers += 1
        if got_numbers > 0:
            ris += (2 ** (got_numbers - 1))

print(ris)

#Part two
ris = 220
card_wins = []

with open('input.txt', 'r') as file:
    for i in range(1, 221):
        numbers = file.readline().strip().replace("Card {:3d}: ".format(i), '').split(' | ')
        winning_numbers = []
        for n in numbers[0].split(' '):
            if n != '':
                winning_numbers.append(n)
        got_numbers = 0
        for n in numbers[1].split(' '):
            if n in winning_numbers:
                got_numbers += 1
        card_wins.append(got_numbers)

got_card = {_ : 1 for _ in range(220)}
for i in range(220):
    ris += card_wins[i] * got_card[i]
    for j in range(i + 1, i + card_wins[i] + 1):
        got_card[j] += got_card[i]

print(ris)
