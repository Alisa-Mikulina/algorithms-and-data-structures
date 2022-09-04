# n = 10 ** 5
# heap = [i + 1 for i in range(n)]
# heap[-1] = -1

# heap = [4, -1, 4, 1, 1]
# n = 5

# heap = [-1, 0, 4, 0, 3]
# n = 5

# heap = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
# n = 10

with open('24.txt', 'r') as f:
    n = f.readline()
    n = int(n)
    heap = f.readline().split(' ')
    for i in range(len(heap)):
        heap[i] = int(heap[i])

heap_len = [0 for i in range(n)]
max_depth = 0

if len(heap) == 1:
    print(max_depth)
else:
    for i in range(len(heap)):
        now = i
        temporary = []

        while True:
            if heap[now] == -1:
                heap_len[now] = 1
            temporary.append(now)
            if heap_len[now] == 0:
                now = heap[now]
            else:
                break
        
        for j in range(len(temporary) - 2, -1, -1):
            heap_len[temporary[j]] = heap_len[temporary[j + 1]] + 1
            if heap_len[temporary[j]] > max_depth:
                max_depth = heap_len[temporary[j]]
            
    print(max_depth)