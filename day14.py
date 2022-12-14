from aocd.models import Puzzle

def a(data):
    _ = ["498,4 -> 498,6 -> 496,6",
            "503,4 -> 502,4 -> 502,9 -> 494,9"]

    min_x = 1000
    max_x = max_y = 0

    # Scan input data for dimensions
    for d in data:
        for dd in d.split(' -> '):
            x,y = map(int, dd.split(','))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    
    grid = [['.']*(max_x - min_x+1) for _ in range(max_y+1)]
    
    # Build grid
    for d in data:
        arrows = d.split(' -> ')

        for idx in range(1, len(arrows)):
            start, end = arrows[idx-1:idx+1]
            
            sx,sy = map(int, start.split(','))
            ex,ey = map(int, end.split(','))

            if sx == ex:
                # Up down line
                for y in range(min(sy, ey), max(sy, ey)):
                    grid[y][sx-min_x] = '#'
            else:
                for x in range(min(sx, ex), max(sx, ex)+1):
                    grid[sy][x-min_x] = '#'

    # Simulate sand
    abyss = False
    sand = 0

    while not abyss:
        sand += 1
        blocked = False
        sx, sy = 500, 0
        
        # Per kernel
        while not blocked:
            if sx-min_x-1 < 0 or sx+1 > max_x or sy == max_y:
                # Out of bounds
                return sand - 1 
            elif grid[sy+1][sx-min_x] == ".":
                # Fall down one if there is space
                sy += 1
            elif grid[sy+1][sx-min_x-1] == ".":
                # Fall left diagonally if there is space
                sy += 1
                sx -= 1
            elif grid[sy+1][sx-min_x+1] == ".":
                # Fall right diagonally if there is space
                sy += 1
                sx += 1
            else:
                blocked = True

        # Fill grid with sand instead of empty space
        grid[sy][sx-min_x] = 'o'
        
def b(data):
    _ = ["498,4 -> 498,6 -> 496,6",
            "503,4 -> 502,4 -> 502,9 -> 494,9"]

    min_x = 10000
    max_x = max_y = 0

    # Scan input data for dimensions
    for d in data:
        for dd in d.split(' -> '):
            x,y = map(int, dd.split(','))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    
    max_y += 2  # Add an extra two rows for part b

    grid = [['.']*(max_x - min_x +1) for _ in range(max_y+1)]
    grid[max_y] = ['#']*(max_x - min_x +1) # Set floor for part b
    
    # Build grid
    for d in data:
        arrows = d.split(' -> ')

        for idx in range(1, len(arrows)):
            start, end = arrows[idx-1:idx+1]
            
            sx,sy = map(int, start.split(','))
            ex,ey = map(int, end.split(','))

            if sx == ex:
                # Up down line
                for y in range(min(sy, ey), max(sy, ey)):
                    grid[y][sx-min_x] = '#'
            else:
                for x in range(min(sx, ex), max(sx, ex)+1):
                    grid[sy][x-min_x] = '#'


    # Simulate sand
    sand = 0

    # Continue simulating sand until the 500,0 is occupied by a sand kernel
    while grid[0][500-min_x] != 'o':
        sand += 1
        blocked = False
        sx, sy = 500, 0
        
        # Drop kernel step-by-step until gets blocked.
        while not blocked:
            # If the sand x coord is heading out of bounds to the left, add an extra column to the left
            if sx-min_x-1 < 0:
                # Ensure min_x in graph is updated after we add a new column
                # (Del)ta between min and max increases by 1
                min_x -= 1

                # Increase grid to left
                for idx, g in enumerate(grid):
                    if idx == max_y:
                        g.insert(0,'#') # Maintain floor
                    else:
                        g.insert(0,'.')
            # If the sand x coord is heading out of bounds to the right, add an extra column to the right
            elif sx+1 > max_x:
                # Ensure (Del)ta x increases 
                max_x += 1
                # Increase grid to right
                for idx, g in enumerate(grid):
                    if idx == max_y:
                        g.append('#') # Maintain floor
                    else:
                        g.append('.')

            # Part b adds an additional exit condition; if the sand kernel reaches the floor
            if sy == max_y - 1:
                blocked = True
            elif grid[sy+1][sx-min_x] == ".":
                # Fall down one if there is space
                sy += 1
            elif grid[sy+1][sx-min_x-1] == ".":
                # Fall left diagonally if there is space
                sy += 1
                sx -= 1
            elif grid[sy+1][sx-min_x+1] == ".":
                # Fall right diagonally if there is space
                sy += 1
                sx += 1
            else:
                blocked = True

        # Current kernel is now blocked, so assign its location
        grid[sy][sx-min_x] = 'o'

    return sand
        
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=14)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))
