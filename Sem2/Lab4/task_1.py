def find_instances(to_find, text):
    inst = ''
    count = 0
    len_f = len(to_find)
    len_t = len(text)
    iterable = len_t - (len_f - 1)
    for i in range(iterable):
        comparable = text[i:i + len_f]
        if comparable == to_find:
            count += 1
            inst += str(i + 1) + ' '
    inst = inst[:-1]
    return [count, inst]




with open('input.txt') as f:
    to_find = f.readline().strip()
    text = f.readline().strip()

ans = find_instances(to_find, text)

with open('output.txt', 'w') as d:
    d.write(str(ans[0]) + '\n')
    d.write(ans[1])