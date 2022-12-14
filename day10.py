from aocd.models import Puzzle

def a(data):
    register = 1
    signal_strength = 0
    cycle = 0    
    
    cycles = [20, 60, 100, 140, 180, 220]
    
    for d in data:
        if d == 'noop':
            cycle += 1
            if cycle in cycles:
                signal_strength += (register * cycle)
                print(cycle, register)
        else:
            instr, val = d.split(' ')
            
            for i in range(2):
                cycle += 1
                
                if cycle in cycles:
                    signal_strength += (register * cycle)
                    print(cycle, register)
            
            register += int(val)
        
    return signal_strength

def b(data):
    w, h = 40, 6
    grid = [['.' for x in range(w)] for y in range(h)]
    
    register = 1
    cycle = 0   # This is needed so that the first
    
    row = 0
    
    for d in data:
        if d == 'noop':
            # Check row for cycle
            if cycle in range(40):
                row = 0
            elif cycle in range(40, 80):
                row = 1
            elif cycle in range(80, 120):
                row = 2
            elif cycle in range(120, 160):
                row = 3
            elif cycle in range(160, 200):
                row = 4
            elif cycle in range(200, 240):
                row = 5
            
            # Calculate if cycle needs to be render
            if cycle-(40*row) in [register-1, register, register+1]:
                grid[row][cycle-(40*row)] = '#'
                
            cycle += 1
                
        else:
            instr, val = d.split(' ')
            
            for i in range(2):
                # Check row for cycle
                if cycle in range(40):
                    row = 0
                elif cycle in range(40, 80):
                    row = 1
                elif cycle in range(80, 120):
                    row = 2
                elif cycle in range(120, 160):
                    row = 3
                elif cycle in range(160, 200):
                    row = 4
                elif cycle in range(200, 240):
                    row = 5
                
                # Calculate if cycle needs to be render
                if cycle-(40*row) in [register-1, register, register+1]:
                    grid[row][cycle-(40*row)] = '#'
                        
                cycle += 1

            register += int(val)
    
    for g in grid:
        print("".join(g))
        
    return 0

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=10)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))