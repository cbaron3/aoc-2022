from aocd.models import Puzzle
from collections import deque

def a(data):
    # data = [
    #     "Sabqponm",
    #     "abcryxxl",
    #     "accszExk",
    #     "acctuvwj",
    #     "abdefghi"
    # ]

    # Find start points
    rows = len(data)
    cols = len(data[0])

    S_x = S_y = None
    E_x = E_y = None
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 'S':
                S_x, S_y = r,c
                data[r] = data[r].replace('S', 'a')
            if data[r][c] == 'E':
                E_x, E_y = r,c
                data[r] = data[r].replace('E', 'z')

    visited = set()

    queue = []
    queue.append((S_x, S_y, 0, 'a')) # Encode start as 'a'

    while queue:
        # Pop queue. Val is really only needed for the very first element
        r, c, d, val = queue.pop(0)

        # Check if we found the element
        if r == E_x and c == E_y:
            return d
        
        # Traverse to all neighbors
        for rr, cc in [(r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)]:
            # First check bounds so we can access data effectively
            if 0 <= rr < rows and 0 <= cc < cols:
                # Then check if neighbor is either equal or one more
                if ord(data[rr][cc]) - ord(val) <= 1:
                    # Then ensure we aren't re-visiting a node
                    if (rr,cc) not in visited:
                        visited.add((rr, cc))
                        queue.append((rr, cc, d + 1, data[rr][cc]))


def b(data):
    # data = [
    #     "Sabqponm",
    #     "abcryxxl",
    #     "accszExk",
    #     "acctuvwj",
    #     "abdefghi"
    # ]

    # Find start points
    rows = len(data)
    cols = len(data[0])

    starting_points = []
    E_x = E_y = None
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 'a':
                starting_points.append((r,c))
            if data[r][c] == 'S':
                starting_points.append((r,c))
                data[r] = data[r].replace('S', 'a')
            if data[r][c] == 'E':
                E_x, E_y = r,c
                data[r] = data[r].replace('E', 'z')

    min_dist = 10000
    for sx,sy in starting_points:
        visited = set()

        queue = []
        queue.append((sx, sy, 0, 'a')) # Encode start as 'a'

        while queue:
            # Pop queue. Val is really only needed for the very first element
            r, c, d, val = queue.pop(0)

            # Check if we found the element
            if r == E_x and c == E_y:
                min_dist = min(min_dist,d)
                break
            
            # Traverse to all neighbors
            for rr, cc in [(r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)]:
                # First check bounds so we can access data effectively
                if 0 <= rr < rows and 0 <= cc < cols:
                    # Then check if neighbor is either equal or one more
                    if ord(data[rr][cc]) - ord(val) <= 1:
                        # Then ensure we aren't re-visiting a node
                        if (rr,cc) not in visited:
                            visited.add((rr, cc))
                            queue.append((rr, cc, d + 1, data[rr][cc]))
    return min_dist
        
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=12)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))
