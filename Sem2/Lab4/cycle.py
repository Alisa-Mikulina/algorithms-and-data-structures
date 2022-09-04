def cycle(initial, final):
    if initial == final:
        return 0
    len_str = len(initial)
    temp = initial
    for i in range(len_str):
        temp = temp[-1:] + temp[:-1]
        if temp == final:
            return i + 1
    return -1




with open('input_cycle.txt') as f:
    initial = f.readline().strip()
    final = f.readline().strip()

ans = cycle(initial, final)

with open('output_cycle.txt', 'w') as d:
    d.write(str(ans))