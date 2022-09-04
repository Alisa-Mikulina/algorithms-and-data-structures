class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def find(self, query):
        local_head = self.head
        while local_head is not None:
            if local_head.data == query:
                return query
            local_head = local_head.next

        return None

    def insert_at(self, at, element):
        local_head = self.head
        new = Node(element)

        while local_head is not None:
            if local_head.data == at:
                new.next = local_head.next
                local_head.next = new
                return

            local_head = local_head.next

    def delete_at(self, at):
        local_head = self.head

        while local_head.next is not None:
            if local_head.data == at:
                next_new = local_head.next
                local_head.next = next_new.next
                return

            local_head = local_head.next
        return

a = LinkedList()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
print(a.to_array())
a.pop()
print(a.to_array())
print(a.find(3))
print(a.find(4))
a.insert_at(2, 5)
print(a.to_array())
a.insert_at(5, 8)
print(a.to_array())
a.delete_at(None)
print(a.to_array())
a.delete_at(5)
print(a.to_array())