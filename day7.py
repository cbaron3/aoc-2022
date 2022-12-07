from aocd.models import Puzzle

total = 0

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.size = 0

def build_tree(data):
    parent_dir = Directory("/", None)
    start_dir = parent_dir
    counter = 0

    for d in data:
        cmd = d.split(" ")
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == "..":
                    parent_dir = parent_dir.parent
                elif cmd[2] == "/":
                    pass
                else:
                    for child in parent_dir.dirs:
                        if cmd[2] == child.name:
                            parent_dir = child

            elif cmd[1] == 'ls':
                pass # Do nothing
        elif cmd[0] == "dir":
            # Add dir to parent
            parent_dir.dirs.append(Directory(cmd[1], parent_dir))
        else:
            parent_dir.size += int(cmd[0])

            node = parent_dir
            while node.parent != None:
                counter+=1
                node.parent.size += int(cmd[0])
                node = node.parent

    return start_dir

def a(data):
    # Build tree
    root = build_tree(data)

    # Basic DFS to accumulate sizes of dirs less than limit
    total = 0
    stack = []
    stack.append(root)

    while (len(stack)):
        root = stack[-1]
        stack.pop()

        if root.size < 100000:
            total += root.size

        for node in root.dirs:
            stack.append(node)

    return total


def b(data):
    # Build tree
    node = build_tree(data)

    # Basic DFS tracking file size of directory with minimum acceptable value to free up enough space
    max_sz = node.size
    min_delete = 1000000000

    stack = []
    stack.append(node)

    while (len(stack)):
        node = stack[-1]
        stack.pop()
        
        if node.size >= max_sz - 40000000:
            min_delete = min(min_delete, node.size)

        for node in node.dirs:
            stack.append(node)

    return min_delete

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=7)

    import time
    start = time.time()

    print('a: {}'.format(a(puzzle.input_data.split('\n'))))
    print('b: {}'.format(b(puzzle.input_data.split('\n'))))

    total = (time.time() - start)
    print('Execution time in seconds: ' + str(total))