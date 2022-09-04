from binary_tree import BinaryTree


tree = BinaryTree()
with open("input_5.txt") as f:
    for line in f.readlines():
        func, elem = line.split()
        elem = int(elem)
        if func == 'insert':
            tree.insert(elem)
        elif func == 'exists':
            whether_found, elem = tree.find(elem)
            print(whether_found)
        elif func == 'delete':
            tree.delete(elem)
        elif func == 'next':
            print(tree.next_num(elem))
        elif func == 'prev':
            print(tree.prev_num(elem))
        else:
            continue