from treap import Treap



treap = Treap()

with open('input_4.txt') as f:
    for line in f.readlines():
        func, elem = line.split()
        elem = int(elem)
        if func == '+':
            treap.insert(elem)
        if func == '?':
            print(treap.give_kth(elem - 1))