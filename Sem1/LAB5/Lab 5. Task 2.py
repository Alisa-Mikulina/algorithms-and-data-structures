from os import defpath
import sys

sys.setrecursionlimit(1000000000)

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

tree = Tree()
aaa = '9 7 5 5 2 9 9 9 2 -1'
heap = aaa.split(' ')
for i in range(len(heap)):
    heap[i] = int(heap[i])
heap = count_sort(heap)
tree.push(heap[-1][-1], heap[-1][0])
last_added = heap[-1][-1]
for i in range(len(heap) - 1):
    for j in range(len(heap[last_added])):
        tree.push(j, last_added)
        last_added = j
print(tree.to_array())
print(tree.depth())
































# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = None
#         self.children = []


# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def push(self, elem, parent):
#         if parent == -1:
#             self.root = Node(elem)
#             self.parent = None
#             return
        
#         if self.root:
#             new_child = Node(elem)
#             new_child.parent = parent
#             iteration = self.root
#             itr_check = self.root
#             parent_adder(iteration, itr_check, parent, new_child)
#             return

#     def to_array(self):
#         array = []
#         start = self.root
#         array.append(start.data)
#         return turn(array, start)
    
#     def depth(self):
#         if self.root == None:
#             return 0
#         max_length = 1
#         local_counter = 1
#         start = self.root
#         return count_depth(max_length, local_counter, start)


# def count_depth(max_length, local_counter, start):
#     if max_length < local_counter:
#         max_length = local_counter
#     for child in start.children:
#         local_counter += 1
#         new_start = child
#         if new_start.children:
#             return count_depth(max_length, local_counter, new_start)
#     return max_length

# def turn(array: list, start: Node):
#     for child in start.children:
#         array.append(child.data)
#         new_start = child
#         if new_start.children:
#             return turn(array, new_start)
#     return array

# def parent_adder(iteration: Node, itr_check: Node, parent, new_child: Node):
#     if parent == itr_check.data:
#         itr_check.children.append(new_child)
#         return
#     if not iteration.children:
#         return
#     for child in iteration.children:
#         if child.data == parent:
#             child.children.append(new_child)
#             return
#         if child.children:
#             new_iteration = child
#             return parent_adder(new_iteration, itr_check, parent, new_child)
#     return

# def count_sort(array):
#     counts = [[] for i in range(len(array))]
#     for i in range(len(array)):
#         if array[i] == -1:
#             counts[0].insert(0, i)
#             continue
#         counts[i].append(i)
#     return counts


# def count_depth_sorted(array, start, max_length, local_length, start_fixed):
#     if not array[start] or array[start] == start_fixed:
#         if max_length < local_length:
#             max_length = local_length
#             local_length -= 1
#             return
#     for i in range(len(array[start])):
#         new_start = array[start][i]
#         local_length += 1
#         if max_length < local_length:
#             max_length = local_length
#         count_depth_sorted(array, new_start, max_length, local_length, start_fixed)
#     return max_length

# # tree = Tree()

# with open('input.txt', 'r') as f:
#     heap = f.readline().split(' ')
#     heap.pop()

# for i in range(len(heap)):
#     heap[i] = int(heap[i])
# heap = count_sort(heap)
# print(heap)

# max_length = 1
# local_length = 1
# start = heap[0][0]
# start_fixed = start
# print(count_depth_sorted(heap, start, max_length, local_length, start_fixed))


# # tree.push(heap[-1][-1], heap[-1][0])
# # for i in range(len(heap) - 1):
# #     for j in heap[i]:
# #         tree.push(j, i)
# # print(tree.to_array())
# # print(tree.depth())