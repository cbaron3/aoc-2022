from aocd.models import Puzzle

def a(data):
    count = 0
    for d in data:
        pair1, pair2 = d.split(',')

        pair1_lo, pair1_hi = pair1.split('-')
        pair2_lo, pair2_hi = pair2.split('-')
        
        if int(pair2_lo) >= int(pair1_lo) and int(pair2_hi) <= int(pair1_hi):
            count += 1
        elif int(pair1_lo) >= int(pair2_lo) and int(pair1_hi) <= int(pair2_hi):
            count += 1

    return count

def b(data):
    count = 0

    for d in data:
        pair1, pair2 = d.split(',')

        pair1_lo, pair1_hi = pair1.split('-')
        pair2_lo, pair2_hi = pair2.split('-')

        x = range(int(pair1_lo),int(pair1_hi)+1)
        y = range(int(pair2_lo),int(pair2_hi)+1)
        z = list(set(x) & set(y))

        if len(z) > 0:
            count += 1 
    return count

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=4)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))