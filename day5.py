from aocd.models import Puzzle
from collections import defaultdict
import re



def a(data):
    # Create list of lists
    stacks = [[] for _ in range(((len(data[0]) + 1)// 4))]
    result = ["" for _ in range(((len(data[0]) + 1)// 4))]

    for d in data:
        # If line is a move, parse out instructions.
        # Per crate, pop from one stack and append to the next
        if d.find('move') != -1:
            N, src, target = map(int, d[5:].replace(" from ", ",").replace(" to ", ",").split(","))
            
            src_stack = stacks[src-1]
            target_stack = stacks[target-1]

            # Pop and append from src to target N times
            for i in range(int(N)):
                target_stack.append(src_stack.pop())
            
            # Re-cache the tops of the src and target stacks
            if target_stack:
                result[target-1] = target_stack[-1]
            if src_stack:
                result[src-1] = src_stack[-1]

        elif d.find('[') != -1:
            # Insert each stack elemeent
            for idx, i in enumerate(range(0, len(d), 4)):
                if d[i+1:i+2] != ' ':
                    stacks[idx].insert(0, d[i+1:i+2])

    print(''.join(result))
    return 0

def b(data):
    # Create list of lists
    stacks = [[] for _ in range(((len(data[0]) + 1)// 4))]
    result = ["" for _ in range(((len(data[0]) + 1)// 4))]

    for d in data:
        # If line is a move, parse out instructions.
        # Per crate, pop from one stack and append to the next
        if d.find('move') != -1:
            N, src, target = map(int, d[5:].replace(" from ", ",").replace(" to ", ",").split(","))
            
            src_stack = stacks[src-1]
            target_stack = stacks[target-1]

            # Instead of popping each element at a time, pop them all first, reverse order, re-add them. Silly approach but works
            container = []
            for i in range(int(N)):
                container.append(src_stack.pop())

            container.reverse()
            for c in container:
                target_stack.append(c)

            # Re-cache the tops of the src and target stacks
            if target_stack:
                result[target-1] = target_stack[-1]
            if src_stack:
                result[src-1] = src_stack[-1]

        elif d.find('[') != -1:
            # Insert each stack elemeent
            for idx, i in enumerate(range(0, len(d), 4)):
                if d[i+1:i+2] != ' ':
                    stacks[idx].insert(0, d[i+1:i+2])

    print(''.join(result))
    return 0


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=5)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))