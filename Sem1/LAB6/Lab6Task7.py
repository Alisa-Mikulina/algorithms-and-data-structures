import time
t_start = time.perf_counter()

def count(stones, pairs, counter):
    ans = 0
    for i in range (len(stones)-1, -1, -1):
        if stones[i] in pairs:
            for next in pairs[stones[i]]:
                if next in counter:
                    ans += counter[next]
        if stones[i] not in counter:
            counter[stones[i]] = 0
        counter[stones[i]] += 1
    print(ans)


with open('input_7.txt') as f:
    lines = f.readlines()

pairs = {}
counter = {}
n, k = map(int, lines[0].split())
stones = lines[1]
for j in range(k):
    pair = lines[2+j]
    if pair[0] not in pairs:
        pairs[pair[0]] = []
    pairs[pair[0]].append(pair[1])
count(stones, pairs, counter)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))