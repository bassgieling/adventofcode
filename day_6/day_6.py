import numpy as np


def solve(part):
    with open('input_6.txt') as f:
        data = [line.strip('\n').strip(' ') for line in f]
        if part == 1:
            data = [[x for x in data[i].split(' ')[1:] if x != ''] for i in range(len(data))]
        elif part == 2:
            data = [[''.join([x for x in data[i].split(' ')[1:] if x != ''])] for i in range(len(data))]

    product = 1
    for i in range(len(data[0])):
        T = int(data[0][i])
        g = int(data[1][i])

        x1 = np.floor((- (-T) - np.sqrt((-T) ** 2 - 4 * 1 * g)) / (2 * 1) + 1)
        x2 = np.ceil((- (-T) + np.sqrt((-T) ** 2 - 4 * 1 * g)) / (2 * 1) - 1)

        product *= int(x2 - x1 + 1)

    print(product)


if __name__ == '__main__':
    solve(1)
    solve(2)
