def separate_into_three(num_suvs, suvs):
    suvs = sorted(suvs)
    if sum(suvs) % 3 != 0 or num_suvs < 3:
        return 0
    equal_cost = sum(suvs) // 3
    counts = [[[0 for k in range(equal_cost + 1)] for j in range(equal_cost + 1)] for i in range(num_suvs + 1)]
    to_add = suvs[0]
    counts[0][to_add][0] = 1
    counts[0][0][to_add] = 1
    counts[0][0][0] = 1
    for i in range(0, num_suvs):
        for j in range(equal_cost + 1):
            for k in range(equal_cost + 1):
                to_add = suvs[i]
                if counts[i][j][k] == 1:
                    if j + to_add <= equal_cost:
                        counts[i + 1][j + to_add][k] = 1
                    if k + to_add <= equal_cost:
                        counts[i + 1][j][k + to_add] = 1
                    if i + 1 < num_suvs:
                        counts[i + 1][j][k] = 1

    return counts[num_suvs][equal_cost][equal_cost]




with open('input_13.txt') as f:
    num_suvs = int(f.readline())
    suvs  = list(map(int, f.readline().split()))

ans = separate_into_three(num_suvs, suvs)
print(ans)
