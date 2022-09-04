class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []


class Tree:
    def __init__(self):
        self.root = None
    
    def push(self, elem, parent):
        if parent == -1:
            self.root = Node(elem)
            self.parent = None
            return
        
        if self.root:
            new_child = Node(elem)
            new_child.parent = parent
            iteration = self.root
            itr_check = self.root
            parent_adder(iteration, itr_check, parent, new_child)
            return

    def to_array(self):
        array = []
        start = self.root
        array.append(start.data)
        return turn(array, start)
    
    def depth(self):
        if self.root == None:
            return 0
        max_length = 1
        local_counter = 1
        start = self.root
        return count_depth(max_length, local_counter, start)


def count_depth(max_length, local_counter, start):
    if max_length < local_counter:
        max_length = local_counter
    for child in start.children:
        local_counter += 1
        new_start = child
        if new_start.children:
            return count_depth(max_length, local_counter, new_start)
    return max_length

def turn(array: list, start: Node):
    for child in start.children:
        array.append(child.data)
        new_start = child
        if new_start.children:
            return turn(array, new_start)
    return array

def parent_adder(iteration: Node, itr_check: Node, parent, new_child: Node):
    if parent == itr_check.data:
        itr_check.children.append(new_child)
        return
    if not iteration.children:
        return
    for child in iteration.children:
        if child.data == parent:
            child.children.append(new_child)
            return
        if child.children:
            new_iteration = child
            return parent_adder(new_iteration, itr_check, parent, new_child)
    return

def count_sort(array):
    counts = [[] for i in range(len(array) + 1)]
    ans = []
    for i in range(len(array)):
        if array[i] == -1:
            counts[-1].append(-1)
            counts[-1].append(i)
            continue
        counts[array[i]].append(i)
    return counts