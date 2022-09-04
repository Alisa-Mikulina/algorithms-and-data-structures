def sortirovka_podschetom(massive):
    low, high = min(massive), max(massive)
    counts = [0 for i in range(max(massive) + 1)]
    ans = []
    for i in range(low, high + 1):
        for char in massive:
            if char == i:
                counts[i] += 1

    for i in range(len(counts)):
        if i >= 0:
            for j in range(counts[i]):
                ans.append(i)
    return ans



aaa = '1 0 4 0 3'
line = aaa.split(' ')
for i in range(len(line)):
    line[i] = int(line[i])

print(sortirovka_podschetom(line))