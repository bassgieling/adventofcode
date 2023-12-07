import numpy as np


def solve(part, prnt=True):
    if part == 1:
        cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'dummy']
    else:
        cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    with open('input_7.txt') as f:
        data = [line.strip('\n').strip(' ') for line in f]
        data = [[x for x in data[i].split(' ')] for i in range(len(data))]

    appearances = []
    for hand, bid in data:
        appearances.append([hand.count(cards[i]) for i in range(len(cards))])

    types = []
    for counts in appearances:
        match np.max(counts[:-1]) + counts[-1]:
            case 5:
                types.append(0)
            case 4:
                types.append(1)
            case 3:
                if part == 1 and 2 in counts[:-1]:
                    types.append(2)
                elif part == 1:
                    types.append(3)
                elif part == 2 and counts[:-1].count(2) == 2:
                    types.append(2)
                elif part == 2 and 3 in counts[:-1] and 2 in counts[:-1]:
                    types.append(2)
                else:
                    types.append(3)
            case 2:
                if counts[:-1].count(2) == 2:
                    types.append(4)
                else:
                    types.append(5)
            case 1:
                types.append(6)

    types, appearances, data = (list(x) for x in zip(*sorted(zip(types, appearances, data))))

    data_ordered = []
    types_ordered = []
    for pack, hand_type in zip(data, types):
        hand, bid = pack[0], pack[1]
        inserted = False
        for i in range(len(data_ordered)):
            if hand_type == types_ordered[i]:
                card = 0
                while hand[card] == data_ordered[i][0][card]:
                    card += 1
                if cards.index(hand[card]) < cards.index(data_ordered[i][0][card]):
                    data_ordered.insert(i, [hand, bid])
                    types_ordered.insert(i, hand_type)
                    inserted = True
                    break
        if not inserted:
            data_ordered.append([hand, bid])
            types_ordered.append(hand_type)

    n = len(data)
    payouts = [(n-i)*int(data_ordered[i][1]) for i in range(n)]
    answer = sum(payouts)
    if prnt:
        print(answer)


if __name__ == '__main__':
    solve(1)
    solve(2)

    import timeit

    t = timeit.timeit('solve(1, prnt=False)', globals=globals(), number=100)
    print(t / 1000)
    t = timeit.timeit('solve(2, prnt=False)', globals=globals(), number=100)
    print(t / 1000)
