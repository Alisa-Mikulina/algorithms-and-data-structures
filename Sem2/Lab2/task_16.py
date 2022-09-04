from binary_tree import BinaryTree



tree = BinaryTree()
ans = []

with open('input_16.txt') as f:
    num_operations = int(f.readline())
    for i in range(num_operations):
        func, elem = f.readline().split()
        elem = int(elem)
        if func == '+1':
            tree.insert(elem)
        elif func == '-1':
            tree.delete(elem)
        elif func == '0':
            ans.append(tree.find_kth_max(elem))

for smol_ans in ans:
    print(smol_ans)