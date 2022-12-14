from aocd.models import Puzzle
from collections import deque
from ast import literal_eval

def get_nested_size(listOfElem):
    count = 0
    # Iterate over the list
    for elem in listOfElem:
        # Check if type of element is list
        if type(elem) == list:  
            # Again call this function to get the size of this element
            count += get_nested_size(elem)
        else:
            count += 1    
    return count

def compare(left, right):
    # Break down lists using recursion to compare element-by-element
    # If all elements are in order value wise, fallback to length of list
    if type(left) == list:
        if type(right) == list:
            for l, r in zip(left, right):
                is_not_equal = compare(l, r)
                if is_not_equal:
                    return is_not_equal
            return len(right) - len(left)
        else:
            return compare(left, [right]) #continuing comparing lists after turning right into list
    else:
        if type(right) == list:
            return compare([left], right) #continuing comparing lists after turning left into list
        else:
            return right - left

def a(data):
    idx = 0
    indices = 0

    for d in range(0,len(data),3):
        left, right = literal_eval(data[d]), literal_eval(data[d+1])

        idx += 1
        if compare(left, right) > 0:
            indices += idx

    return indices

def b(data):
    idx = 0
    indices = 0

    i1 = i2 = 1
    for d in range(0,len(data),3):
        left, right = literal_eval(data[d]), literal_eval(data[d+1])
        
        # Track how many times 2 and 6 are in the correct ordering
        if compare(left, [[2]]) > 0: i1 += 1
        if compare(left, [[6]]) > 0: i2 += 1
        if compare(right, [[2]]) > 0: i1 += 1
        if compare(right, [[6]]) > 0: i2 += 1

    # We know 6 is 1 higher than 2 and since we dont consider them in the comparison, increase i2 by 1
    return (i1)*(i2+1)
        
if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=13)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))
