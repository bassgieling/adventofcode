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
        T = int(data[0][i])  # Time
        g = int(data[1][i])  # goal

        x1 = np.floor((- (-T) - np.sqrt((-T) ** 2 - 4 * 1 * g)) / (2 * 1) + 1)
        x2 = np.ceil((- (-T) + np.sqrt((-T) ** 2 - 4 * 1 * g)) / (2 * 1) - 1)

        product *= int(x2 - x1 + 1)

    # print(product)


if __name__ == '__main__':
    import timeit
    t = timeit.timeit('solve(1)', globals=globals(), number=1000)
    print(t/1000)
    t = timeit.timeit('solve(2)', globals=globals(), number=1000)
    print(t/1000)
