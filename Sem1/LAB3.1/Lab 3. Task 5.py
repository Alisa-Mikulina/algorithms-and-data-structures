import time
t_start = time.perf_counter()

def count_sort(massive):
    low, high = min(massive), max(massive)
    counts = [0 for i in range(max(massive)+1)]
    ans = []
    for i in range(low, high+1):
        for char in massive:
            if char == i:
                counts[i] += 1

    for i in range(len(counts) - 1, -1, -1):
        if i >= 0:
            for j in range(counts[i]):
                ans.append(i)
    return ans

def hirsh_index(citations):
    citations = count_sort(citations)
    i = 0
    while citations[i] > i:
        i += 1
    return i

f = open("input.txt", "r")
citations = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(str(hirsh_index(citations)))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))