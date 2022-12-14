from aocd.models import Puzzle


def a(data):
    xh = yh = xt = yt = 0

    unique_coords = set()

    for d in data:
        motion, sz = d.split(" ")
        
        for _ in range(0, int(sz)):
            # Move H
            if motion == "R": xh += 1
            if motion == "L": xh -= 1
            if motion == "D": yh -= 1
            if motion == "U": yh += 1

            # Bordering; pass
            if abs(xh - xt) <= 1 and abs(yh - yt) <= 1:
                pass
            elif yh-yt == 0 and xh-xt == 2:
                xt += 1
            elif yh-yt == 0 and xh-xt == -2:
                xt -= 1
            elif xh-xt == 0 and yh-yt == 2:
                yt += 1
            elif xh-xt == 0 and yh-yt == -2:
                yt -= 1
            else:  
                # not on same row or column, move diagonally
                if yh-yt > 0:
                    yt += 1
                else:
                    yt -= 1

                if xh-xt > 0:
                    xt += 1
                else:
                    xt -= 1
                

            unique_coords.add((xt, yt))

    return len(unique_coords)
    
def b(data):
    positions = [[0,0] for i in range(10)]
    unique_coords = set()

    for d in data:
        motion, sz = d.split(" ")
        
        for _ in range(0, int(sz)):
            # Move H
            if motion == "R": positions[0][0] += 1
            if motion == "L": positions[0][0] -= 1
            if motion == "D": positions[0][1] -= 1
            if motion == "U": positions[0][1] += 1

            for i in range(9):
                xh, yh = positions[i]
                xt, yt = positions[i+1]

                # Bordering; pass
                if abs(xh - xt) <= 1 and abs(yh - yt) <= 1:
                    pass
                elif yh-yt == 0 and xh-xt == 2:
                    positions[i+1][0] += 1
                elif yh-yt == 0 and xh-xt == -2:
                    positions[i+1][0] -= 1
                elif xh-xt == 0 and yh-yt == 2:
                    positions[i+1][1] += 1
                elif xh-xt == 0 and yh-yt == -2:
                    positions[i+1][1] -= 1
                else:  
                    # not on same row or column, move diagonally
                    if yh-yt > 0:
                        positions[i+1][1] += 1
                    else:
                        positions[i+1][1] -= 1

                    if xh-xt > 0:
                        positions[i+1][0] += 1
                    else:
                        positions[i+1][0] -= 1
                    

            unique_coords.add(tuple(positions[9]))

    return len(unique_coords)
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=9)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))
