from aocd.models import Puzzle

def a(data):
    for idx, d in enumerate(data[0]):
        if len(set(data[0][idx:idx+4])) == 4:
            return idx+4

def b(data):
    for idx, d in enumerate(data[0]):
        if len(set(data[0][idx:idx+14])) == 14:
            return idx+14

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=6)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))