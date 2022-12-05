from aocd.models import Puzzle

def a(data):
    curr_elf = 0
    max_elf = 0

    for d in data:
        if d == '':
            max_elf = max(max_elf, curr_elf)
            curr_elf = 0
        else:
            curr_elf += int(d)
    return max_elf

def b(data):
    curr = 0
    results = []

    for d in data:
        if d == '':
            results.append(curr)
            curr = 0
        else:
            curr += int(d)
    
    results.sort()
    
    return sum(results[-3:])

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))