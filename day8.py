from aocd.models import Puzzle

def a(data):

    rows = len(data[0])
    cols = len(data)

    visible = 0

    for c in range(cols):
        for r in range(rows):
            if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                # At edge
                visible += 1
            else:
                is_visible = 4
                for cc in range(c):
                    if data[cc][r] >= data[c][r]:
                        is_visible -=1
                        break


                for cc in range(c+1, cols):
                    if data[cc][r] >= data[c][r]:
                        is_visible -=1
                        break

                for rr in range(r):
                    if data[c][rr] >= data[c][r]:
                        is_visible -=1
                        break

                for rr in range(r+1, rows):
                    if data[c][rr] >= data[c][r]:
                        is_visible -=1
                        break
            
                if is_visible > 0:
                    visible += 1

    return visible

       

def b(data):


    rows = len(data[0])
    cols = len(data)

    max_scenic_score = 0

    for c in range(cols):
        for r in range(rows):
            scenic_score = 1

            if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                # At edge
                scenic_score = 0
            else:
                visible_trees = 0
                for cc in range(c-1, -1, -1):
                    visible_trees += 1
                    if data[cc][r] >= data[c][r]:
                        break
                scenic_score *= visible_trees

                visible_trees = 0
                for cc in range(c+1, cols):
                    visible_trees += 1
                    if data[cc][r] >= data[c][r]:
                        break
                scenic_score *= visible_trees

                visible_trees = 0
                for rr in range(r-1, -1, -1):
                    visible_trees += 1
                    if data[c][rr] >= data[c][r]:
                        break
                scenic_score *= visible_trees

                visible_trees = 0
                for rr in range(r+1, rows):
                    visible_trees += 1
                    if data[c][rr] >= data[c][r]:
                        break
                scenic_score *= visible_trees

                max_scenic_score = max(scenic_score, max_scenic_score)

    return max_scenic_score
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=8)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))