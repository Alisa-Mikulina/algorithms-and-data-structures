def separate_into_two(num_elms, elms):
    if sum(elms) % 2 != 0:
        return -1
    expected_sum = sum(elms) // 2
    first = []
    second = []
    elms = sorted(elms)
    for i in range(len(elms) - 1, -1, -1):
        if sum(first) < sum(second):
            first.append(elms[i])
        else:
            second.append(elms[i])
    if sum(first) == expected_sum and sum(second) == expected_sum:
        return f'{sum(first)} \n{first}'
    else:
        return -1



with open('input_12.txt') as f:
    num_elms = int(f.readline())
    elms  = list(map(int, f.readline().split()))

ans = separate_into_two(num_elms, elms)
print(ans)