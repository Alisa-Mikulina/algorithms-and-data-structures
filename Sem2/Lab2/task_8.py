# I solemnly swear I'm okay having taken 2 energetic drinks and botating at 2am...
# I wish I could just import the tree from my amazing file but I can't cause it will not be accepted by openedu this way
# Hochetsya spat'
class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None
    

    def insert(self, new):
        if self.root == None:
            new_root = Node(new)
            self.root = new_root
            return
        
        new_node = Node(new)
        whether_found, parent = self.find(new)
        parent_value = parent.data
        new_node.parent = parent
        if new > parent_value:
            parent.right = new_node
            return
        parent.left = new_node
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

with open('input_8.txt') as f:
    num_nodes = int(f.readline())
    for i in range(num_nodes):
        new_node, smth, smth_else = f.readline().split()
        new_node = int(new_node)
        tree.insert(new_node)


with open('output_8.txt', 'w') as d:
    depth = tree.depth()
    d.write(str(depth))




        # def depth(self, rut='aa'):
    #     count = 0
    #     left = 0
    #     right = 0
    #     if rut == 'aa':
    #         rut = self.root
    #     if rut == None:
    #         return 0
    #     if rut != None and rut.left == None and rut.right == None:
    #         return 1
    #     if rut.left != None:
    #         if rut.left.left != None and rut.left.right == None:
    #             left += 1
    #             while rut.left.left != None and rut.left.right == None:
    #                 rut = rut.left
    #                 left += 1
    #             if rut.left.right != None:
    #                 left = 1 + self.go_inside(rut.left)
    #         else:
    #             left = 1 + self.go_inside(rut.left)
    #     if rut.right != None:
    #         if rut.right.right != None and rut.right.left == None:
    #             right += 1
    #             while rut.right.right != None and rut.right.left == None:
    #                 rut = rut.right
    #                 right += 1
    #             if rut.right.left != None:
    #                 right = 1 + self.go_inside(rut.right)
    #         else:
    #             right = 1 + self.go_inside(rut.right)
    #     count += max(left, right)
    #     if count == 0:
    #         return 0
    #     else:
    #         return count + 1
    

    # def go_inside(self, rut):
    #     left = 0
    #     right = 0
    #     if rut == None:
    #         return 0
    #     if rut.left == None and rut.right == None:
    #         return 0 
    #     if rut.left != None:
    #         if rut.left.left != None and rut.left.right == None:
    #             left += 1
    #             while rut.left.left != None and rut.left.right == None:
    #                 rut = rut.left
    #                 left += 1
    #             if rut.left.right != None:
    #                 left = 1 + self.go_inside(rut.left)
    #         else:
    #             left = 1 + self.go_inside(rut.left)
    #     if rut.right != None:
    #         if rut.right.right != None and rut.right.left == None:
    #             right += 1
    #             while rut.right.right != None and rut.right.left == None:
    #                 rut = rut.right
    #                 right += 1
    #             if rut.right.left != None:
    #                 right = 1 + self.go_inside(rut.right)
    #         else:
    #             right = 1 + self.go_inside(rut.right)
    #     return max(left, right)