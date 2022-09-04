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
    

    def delete(self, query):
        whether_found, rut = self.find(query)

        # If there is no such node
        if whether_found == False:
            print('none')
            return
        
        # If the node to delete has no chindren
        if rut.left == None and rut.left == None:
            parent_value = rut.parent.data
            parent = rut.parent
            if query < parent_value:
                print(rut.parent.left)
                rut.parent.left = None
                self.num_nodes -= 1
                return rut
            rut.parent.right = None
            self.num_nodes -= 1
            return rut
        
        # If the node has only one child
        if rut.left != None and rut.right == None:
            parent_value = rut.parent.data
            if query < parent_value:
                rut.parent.left = rut.left
                self.num_nodes -= 1
                return
            rut.parent.right = rut.left
            self.num_nodes -= 1
            return
        elif rut.left == None and rut.right != None:
            parent_value = rut.parent.data
            if query < parent_value:
                rut.parent.left = rut.right
                self.num_nodes -= 1
                return
            rut.parent.right = rut.right
            self.num_nodes -= 1
            return
        
        # If the node has 2 children
        if rut.left and rut.right:
            minimum = self.find_min(rut.right)
            whether_found, node = self.find(minimum)
            before_node = node.parent
            if before_node.left.data == node.data:
                before_node.left = None
            else:
                before_node.right = None
            node.right = rut.right
            node.left = rut.left
            parent = rut.parent
            self.num_nodes -= 1

            if parent == None:
                self.root = node
                return
            node.parent = parent
            if rut.data == parent.data:
                parent.left = node
                return
            parent.right = node
            return
    

    def next_num(self, num, rut='aa'):
        if rut == 'aa':
            rut = self.root
        if rut == None:
            return 'none'
        if rut.left == None and rut.right == None and rut.data <= num:
            return 'none'
        elif rut.data == num:
            if rut.right != None:
                return self.next_num(num, rut.right)
            else:
                if rut.parent.data < num:
                    return rut.parent.data
                else:
                    return 'none'
        elif rut.data > num:
            if (rut.data - num) == 1:
                return rut.data
            if rut.left == None:
                return rut.data
            if rut.left.data == num:
                if rut.left.right == None:
                    return rut.data
                else:
                    return self.next_num(num, rut.left.right)
            if rut.left.data:
                return self.next_num(num, rut.left)
        elif rut.data < num:
            return self.next_num(num, rut.right)
        else:
            return self.next_num(num, rut.left)
        

    def prev_num(self, num, rut='aa'):
        if rut == 'aa':
            rut = self.root
        if rut == None:
            return 'none'
        if rut.left == None and rut.right == None and rut.data > num:
            return 'none'
        elif rut.data == num:
            if rut.left != None:
                return self.prev_num(num, rut.left)
            else:
                if rut.parent.data < num:
                    return rut.parent.data
                else:
                    return 'none'
        if rut.data < num:
            if (num - rut.data) == 1:
                return rut.data
            if rut.right == None:
                return rut.data
            if rut.right.data == num:
                if rut.right.left == None:
                    return rut.data
                else:
                    return self.prev_num(num, rut.right.left)
            if rut.right.data:
                return self.prev_num(num, rut.right)
        if rut.data > num:
            if rut.left.data == num:
                if rut.left.left:
                    return self.prev_num(num, rut.left)
                else:
                    if rut.parent.data < num:
                        return rut.parent.data
                    else:
                        return 'none'
            return self.prev_num(num, rut.left)
        else:
            return self.prev_num(num, rut.right)
    

    def find_min(self, rut):
        if rut.left:
            min_cur = rut.left.data
            next_rut = rut.left
            minimum = min(min_cur, self.find_min(next_rut))
            return minimum
        if not rut.right or rut.left:
            return(rut.data)
    

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


    def find_kth_max(self, k):
        rut = self.root
        while rut.right != None:
            rut = rut.right
        max_decreased = []
        max_decreased.append(rut.data)
        current_max = 1
        returned = self.kth_max_assistant(rut, k, current_max)
        current_max = returned[1]
        max_decreased += returned[0]
        while current_max < k:
            if rut.parent:
                rut = rut.parent
                max_decreased.append(rut.data)
                returned = self.kth_max_assistant(rut, k, current_max)
                current_max = returned[1]
                max_decreased += returned[0]
            elif rut.left:
                max_decreased.append(rut.left.data)
                returned = self.kth_max_assistant(rut, k, current_max)
                current_max = returned[1]
                max_decreased += returned[0]
        return max_decreased[k - 1]


    def kth_max_assistant(self, rut, k, current_max, kth=1):
        to_add = []
        if rut.right == None and rut.left == None:
            return [to_add, current_max]
        if rut.right != None and kth != 1:
            current_max += 1
            returned = self.kth_max_assistant(rut.right, k, current_max, kth + 1)
            to_add += returned[0]
            to_add.append(rut.right.data)
            current_max = returned[1]
        if rut.left != None:
            current_max += 1
            returned = self.kth_max_assistant(rut.left, k, current_max, kth + 1)
            to_add += returned[0]
            to_add.append(rut.left.data)
            current_max = returned[1]
        return [to_add, current_max]

    
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






# my_tree = BinaryTree()

# my_tree.insert(2)
# my_tree.insert(3)
# my_tree.insert(50)
# my_tree.insert(200)
# my_tree.insert(400)
# my_tree.insert(30)
# my_tree.insert(35)
# my_tree.insert(40)
# my_tree.insert(45)
# my_tree.insert(37)
# my_tree.insert(32)
# my_tree.insert(20)
# my_tree.insert(12)
# my_tree.insert(4)


# print(my_tree.find_kth_max(1))
# print(my_tree.find_kth_max(2))
# print(my_tree.find_kth_max(3))
# print(my_tree.find_kth_max(4))

# my_tree.insert(8)
# my_tree.insert(4)
# my_tree.insert(12)
# my_tree.insert(2)
# my_tree.insert(10)
# my_tree.insert(14)
# my_tree.insert(3)
# my_tree.insert(5)
# my_tree.insert(7)
# my_tree.insert(11)
# my_tree.insert(13)
# my_tree.insert(15)

# my_tree.insert(-2)
# my_tree.insert(8)
# my_tree.insert(9)
# my_tree.insert(3)
# my_tree.insert(6)
# my_tree.insert(0)

# print(my_tree.count_nodes())

# my_tree.delete(8)
# print(my_tree.num_nodes)

# print(my_tree.delete_subtree(6))
# print(my_tree.delete_subtree(9))
# print(my_tree.delete_subtree(7))
# print(my_tree.delete_subtree(8))

# print(my_tree.next_num(1)) # 2 +
# print(my_tree.next_num(3)) # 4 +
# print(my_tree.next_num(7)) # 8 +
# print(my_tree.next_num(11)) # 12 +
# print(my_tree.next_num(13)) # 14 +
# print(my_tree.next_num(15)) # none +
# print(my_tree.next_num(2)) # 3 +
# print(my_tree.next_num(5)) # 7 +
# print(my_tree.next_num(10)) # 11 +
# print(my_tree.next_num(14)) # 15 +
# print(my_tree.next_num(4)) # 5 +
# print(my_tree.next_num(12)) # 13 +
# print(my_tree.next_num(8)) # 10 +

# print(my_tree.prev_num(3)) # 2 +
# print(my_tree.prev_num(7)) # 5 +
# print(my_tree.prev_num(11)) # 10 +
# print(my_tree.prev_num(13)) # 12 +
# print(my_tree.prev_num(15)) # 14 +
# print(my_tree.prev_num(2)) # none +
# print(my_tree.prev_num(5)) # 4 +
# print(my_tree.prev_num(10)) # 8 +
# print(my_tree.prev_num(14)) # 13 +
# print(my_tree.prev_num(4)) # 3 +
# print(my_tree.prev_num(12)) # 11 +
# print(my_tree.prev_num(8)) # 7 +

# my_tree.printtree()

# found, node = my_tree.find(8)
# print(found, node.data, node.left, node.right)