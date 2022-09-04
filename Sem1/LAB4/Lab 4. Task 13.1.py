class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, element):
        if self.head == None:
            self.head = Node(element)
            return

        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return

        self.head = self.head.next

    def to_array(self):
        array = []
        local_head = self.head
        while local_head is not None:
            array.append(local_head.data)
            local_head = local_head.next
        return array

a = LinkedList()
print(a.is_empty())
a.push(1)
print(a.is_empty())
a.push(2)
a.push(3)
a.push(4)
print(a.to_array())
print(a.is_empty())
a.pop()
a.pop()
a.pop()
a.pop()
print(a.is_empty())