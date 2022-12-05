from aocd.models import Puzzle

scores = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

reverse = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

def foo(data, m):
    total = 0 
    for d in data:
        total += m[d]

    return total

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=2)

    import time
    start = time.time()

    print('a: {}'.format(foo(puzzle.input_data.split('\n'), scores)))
    print('b: {}'.format(foo(puzzle.input_data.split('\n'), reverse)))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))