a = []
for i in range(-1, 10):
    a.append(i)

with open('input.txt', 'w') as f:
    for symb in a:
        f.write(str(symb) + ' ')