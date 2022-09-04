from random import randint

class Node:
    def __init__(self):
        self.data = None
        self.priority = randint(1, 2 ** 64)
        self.left = None
        self.right = None
        self.size = 1




class Treap:
    def __init__(self):
        self.root = None


    def insert(self, elem):
        new_node = Node()
        new_node.data = elem
        if self.root == None:
            self.root = new_node
            return
        if self.if_exists(elem) == True:
            return
        left, right = self.split(self.root, elem - 1)
        self.root = self.merge(left, new_node)
        self.root = self.merge(self.root, right)
        return


    def deepart(self, rut): # it's called deepart because it looks like it will depart me to hell yet it's art
        left = 0
        right = 0
        if rut.left != None:
            left = rut.left.size
        if rut.right != None:
            right = rut.right.size
        return left + right + 1


    def if_exists(self, elem):
        left, right = self.split(self.root, elem - 1)
        if right == None:
            return False
        r = right
        while right.left != None:
            right = right.left
        if right.data != elem:
            self.root = self.merge(left, r)
            return False
        else:
            self.root = self.merge(left, r)
            return True


    def merge(self, left, right):
        if left == None:
            return right
        elif right == None:
            return left
        elif left.priority > right.priority:
            left.right = self.merge(left.right, right)
            ans = left
        else:
            right.left = self.merge(left, right.left)
            ans = right
        ans.size = self.deepart(ans)
        return ans


    def split(self, rut, elem):
        if rut == None:
            return (None, None)
        if elem < rut.data:
            left, rut.left = self.split(rut.left, elem)
            right = rut
            right.size = self.deepart(right)
            return (left, right)
        else:
            rut.right, right = self.split(rut.right, elem)
            left = rut
            left.size = self.deepart(left)
            return (left, right)


    def next_x(self, elem): # WHY ON EARTH IT IS 7 LINES LONG NOT 30
        left, right = self.split(self.root, elem)
        if right == None:
            return 0
        r = right
        while right.left != None:
            right = right.left
        self.root = self.merge(left, r)
        return right.data


    def give_kth(self, k, rut='aa'):
        if rut == 'aa':
            rut = self.root
        if rut.left != None:
            size_l = rut.left.size
        else:
            size_l = 0
        if size_l == k:
            return rut.data
        elif size_l > k:
            rut = rut.left
            return self.give_kth(k, rut)
        elif size_l < k:
            rut = rut.right
            k = k - size_l - 1
            return self.give_kth(k, rut)


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


# treap = Treap()

# treap.insert(2)
# treap.insert(3)
# treap.insert(1)
# treap.insert(4)
# treap.insert(8)
# treap.insert(12)
# treap.insert(6)
# treap.insert(7)
# treap.insert(200)
# treap.insert(13)
# treap.insert(43)
# treap.insert(22)
# treap.insert(111)


# treap.printtree()
# print('')
# print(treap.root.size)
# print('')
# print(treap.give_kth(0))
# print(treap.give_kth(1))
# print(treap.give_kth(2))
# print(treap.give_kth(3))
# print(treap.give_kth(4))
# print(treap.give_kth(5))
# print(treap.give_kth(6))
# print(treap.give_kth(7))
# print(treap.give_kth(8))
# print(treap.give_kth(9))
# print(treap.give_kth(10))
# print(treap.give_kth(11))
# print(treap.give_kth(12))

# # print(treap.next_x(3))