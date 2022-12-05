from aocd.models import Puzzle

def to_ascii(c):
    if c.isupper():
        return ord(c) - 65 + 27
    else:
        return ord(c) - 97 + 1

def a(data):
    total = []
    for d in data:
        total.append([to_ascii(x) for x in set(d[:len(d)//2]) & set(d[len(d)//2:])][0])
    return sum(total)

def b(data):
    # Take list, chunk it into groups of three
    group = []
    total = []
    for d in data:
        group.append(d)

        if len(group) == 3:
            total.append([to_ascii(x) for x in set(group[0]) & set(group[1]) & set(group[2])][0])
            group = []
    return sum(total)

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=3)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))