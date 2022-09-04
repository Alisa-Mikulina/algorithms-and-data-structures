class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right = None
        self.left = None



class BinaryTree:
    def __init__(self):
        self.root = None
        self.num_nodes = 0
    

    def insert(self, new):
        if self.root == None:
            new_root = Node(new)
            self.root = new_root
            self.num_nodes += 1
            return
        
        new_node = Node(new)
        whether_found, parent = self.find(new)
        parent_value = parent.data
        new_node.parent = parent
        if new > parent_value:
            parent.right = new_node
            self.num_nodes += 1
            return
        parent.left = new_node
        self.num_nodes += 1
        return


    def find(self, query, rut='aa'):
        if rut == 'aa':
            rut = self.root
        if rut.data == query:
            return True, rut
        elif query < rut.data and rut.left != None:
            return self.find(query, rut.left)
        elif query > rut.data and rut.right != None:
            return self.find(query, rut.right)
        else:
            return(False, rut)


    def depth(self, rut='aa'):
        count = 0
        left = 0
        right = 0
        if rut == 'aa':
            rut = self.root
        if rut == None:
            return 0
        if rut != None and rut.left == None and rut.right == None:
            return 1
        if rut.left != None:
            left = 1 + self.go_inside(rut.left)
        if rut.right != None:
            right = 1 + self.go_inside(rut.right)
        count += max(left, right)
        if count == 0:
            return 0
        else:
            return count + 1
    

    def go_inside(self, rut):
        left = 0
        right = 0
        if rut.left == None and rut.right == None:
            return 0
        if rut.left != None:
            left = 1 + self.go_inside(rut.left)
        if rut.right != None:
            right = 1 + self.go_inside(rut.right)
        return max(left, right)
    

    def delete_subtree(self, node_id):
        whether_found, node = self.find(node_id)
        if whether_found == False:
            return self.num_nodes
        parent = node.parent
        if parent.data > node.data:
            diff = self.count_nodes(node)
            self.num_nodes -= diff
            parent.left = None
            return self.num_nodes
        elif parent.data < node.data:
            diff = self.count_nodes(node)
            self.num_nodes -= diff
            parent.right = None
            return self.num_nodes


    def count_nodes(self, node='aa'):
        if node == 'aa': 
            node = self.root
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    
    def printtree(self, rut=-1):
        if rut == -1:
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




tree = BinaryTree()

with open('input_9.txt') as f:
    num_nodes = int(f.readline())
    for i in range(num_nodes):
        new_node, smth, smth_else = f.readline().split()
        new_node = int(new_node)
        tree.insert(new_node)
    num_deletions = int(f.readline())
    deletions = list(map(int, f.readline().split()))


with open('output_9.txt', 'w') as d:
    for deletion in deletions:
        d.write(str(tree.delete_subtree(deletion)) + '\n')