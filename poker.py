import random
card = [1, 2, 3]
def bot(card):
    pass
def game(card, player):
    bot1 = int(card[0])
    bot2 = int(card[1])
    player1 = player[0]
    player2 = player[1]
    if player1 == 1:
        print(f'{bot1} is your card')
        ruch1 = int(input('Player1, mises (1) /fold (2): '))
    elif player1 == 2:
        pass
    elif player2 == 3:
        ruch1 = 1
    if player2 == 1:
        print(f'{bot2} is your card')
        ruch2 = int(input('Player2, mises (1) /fold (2): '))
    elif player2 == 2:
        pass
    elif player2 == 3:
        ruch2 = 1
    if ruch1 == 2:
        return -1, 1
    else:
        if ruch2 == 2:
            return 1, -1
        else:
            if bot1 > bot2:
                return 2, -2
            else:
                return -2, 2
mains = []
scores = []
for x in range(3):
    for y in range(2):
        jack = card.copy()
        del jack[x]
        mains.append(f'{card[x]}{jack[y]}')

    
pv1 = 10
pv2 = 10
for x in range(6):
    jack = mains[random.randint(0, 5)]
    c1 = int(jack[0])
    c2 = int(jack[1])
    print(c1, c2)
    linu = game([c1, c2], [3, 3])
    pv1 += linu[0]
    pv2 += linu[1]
    print(f'linu: {linu}/ pv1 {pv1} pv2 {pv2}')
    