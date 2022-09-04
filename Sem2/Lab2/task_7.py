# I honestly hate the way the way adding nodes is described, I have no idea how it could be done easier, 
# but this is painful save me pls I wanna cryyyyyyyyy
import math

class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right = None
        self.left = None


class Tree():
    def __init__(self) -> None:
        self.root = None

    
    def insert(self, nodes, rut, line):
        if line[0] == rut.data:
            if line[1] != -1:
                rut.left = nodes[line[1]]
            if line[2] != -1:
                rut.right = nodes[line[2]]
            return True
        if_inserted = False
        if rut.left != None:
            if_inserted = self.insert(nodes, rut.left, line)
        if if_inserted == True:
            return True
        if rut.right != None:
            return self.insert(nodes, rut.right, line)


    def check_bst(self, rut):
        if rut.left != None:
            if rut.left.data < rut.data:
                if self.max_subtree(rut.left) >= rut.data:
                    return 'INCORRECT'
                self.check_bst(rut.left)
            else:
                return 'INCORRECT'
        if rut.right != None:
            if rut.right.data >= rut.data:
                if self.min_subtree(rut.right) < rut.data:
                    return 'INCORRECT'
                self.check_bst(rut.right)
            else:
                return 'INCORRECT'
        return 'CORRECT'


    def max_subtree(self, rut):
        biggest = -math.inf
        tree = rut
        while tree.left != None:
            if tree.left.data >= biggest:
                biggest = tree.left.data
            tree = tree.left
            tree_ = tree
            while tree.right is not None:
                if tree.right.data > biggest:
                    biggest = tree.right.data
                tree = tree.right
            tree = tree_
        tree = rut
        while tree.right != None:
            if tree.right.data >= biggest:
                biggest = tree.right.data
            tree = tree.right
            tree_ = tree
            while tree.left is not None:
                if tree.left.data > biggest:
                    biggest = tree.left.data
                tree = tree.left
            tree = tree_
        return biggest


    def min_subtree(self, rut):
        smallest = math.inf
        tree = rut
        while tree.left != None:
            if tree.left.data < smallest:
                smallest = tree.left.data
            tree = tree.left
            tree_ = tree
            while tree.right is not None:
                if tree.right.data < smallest:
                    smallest = tree.right.data
                tree = tree.right
            tree = tree_
        tree = rut
        while tree.right != None:
            if tree.right.data < smallest:
                smallest = tree.right.data
            tree = tree.right
            tree_ = tree
            while tree.left is not None:
                if tree.left.data < smallest:
                    smallest = tree.left.data
                tree = tree.left
            tree = tree_
        return smallest


    def printtree(self, rut='aa'):
        if rut == 'aa':
            rut = self.root
        
        to_print = ''
        if rut.left:
            to_print += str(rut.left.data)
        else:
            to_print += 'None'
        
        to_print += '|' + str(rut.data) + '|'

        if rut.right:
            to_print += str(rut.right.data)
        else:
            to_print += 'None'
        print(to_print)

        if rut.left:
            self.printtree(rut.left)
        if rut.right:
            self.printtree(rut.right)
        return




my_tree = Tree()

with open('input_7.txt') as f:
    num_nodes = int(f.readline())
    nodes = {}
    for i in range(num_nodes):
        data, id_left_ch, id_right_ch = list(map(int, f.readline().split()))
        if i == 0:
            new_root = Node(data=data)
            my_tree.root = new_root
        else:
            new_node = Node(data=data)
            nodes[i] = new_node

with open('input_7.txt') as f:
    num_nodes = int(f.readline())
    for i in range(num_nodes):
        line = list(map(int, f.readline().split()))
        my_tree.insert(nodes, my_tree.root, line)

with open('output_7.txt', 'w') as d:
    if num_nodes == 0:
        d.write('CORRECT')
    else:
        d.write(my_tree.check_bst(my_tree.root))