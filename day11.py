from aocd.models import Puzzle
from collections import defaultdict
from math import prod
from copy import deepcopy

items = [
    [66, 59, 64, 51],
    [67, 61],
    [86, 93, 80, 70, 71, 81, 56],
    [94],
    [71, 92, 64],
    [58, 81, 92, 75, 56],
    [82, 98, 77, 94, 86, 81],
    [54, 95, 70, 93, 88, 93, 63, 50],
]

ops = [
    lambda fn: fn * 3,
    lambda fn: fn * 19,
    lambda fn: fn + 2,
    lambda fn: fn * fn,
    lambda fn: fn + 8,
    lambda fn: fn + 6,
    lambda fn: fn + 7,
    lambda fn: fn + 4,
]

divisibles = [2, 7, 11, 19, 3, 5, 17, 13]

true_throws = [1, 3, 4, 7, 5, 3, 7, 2]

false_throws = [4, 5, 0, 6, 1, 6, 2, 0]

def a(data):
    inspections = defaultdict(int)
    
    # Deepcopy required to ensure global items is a read-only copy
    # Fixed bug where part 2 was wrong because part 2 was picking up where part 1 left off
    monkey_items = deepcopy(items)
    
    # 20 rounds of monkey business
    for i in range(20):
        for monkey_idx in range(len(monkey_items)):
            for monkey_item in monkey_items[monkey_idx]:
                inspections[monkey_idx] += 1
                
                worry_value = (ops[monkey_idx](monkey_item)) // 3
                
                if worry_value % divisibles[monkey_idx] == 0:
                    monkey_items[true_throws[monkey_idx]].append(worry_value)
                else:
                    monkey_items[false_throws[monkey_idx]].append(worry_value)
                    
            # After processing items, they can be discarded for next round
            monkey_items[monkey_idx] = []
        
    return prod(sorted(inspections.values())[-2:])

def b(data):
    inspections = defaultdict(int)
    
    monkey_items = deepcopy(items)
    
    the_great_equalizer = prod(divisibles)
    
    # 100000 rounds of monkey business
    for i in range(10000):
        for monkey_idx in range(len(monkey_items)):
            for monkey_item in monkey_items[monkey_idx]:
                inspections[monkey_idx] += 1
                
                worry_value = (ops[monkey_idx](monkey_item)) % the_great_equalizer

                if worry_value % divisibles[monkey_idx] == 0:
                    monkey_items[true_throws[monkey_idx]].append(worry_value)
                else:
                    monkey_items[false_throws[monkey_idx]].append(worry_value)
                    
            # After processing items, they can be discarded for next round
            monkey_items[monkey_idx] = []
        
    return prod(sorted(inspections.values())[-2:])

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=11)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))