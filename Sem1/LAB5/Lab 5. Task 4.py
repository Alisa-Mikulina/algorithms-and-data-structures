def min_heapify(i, heap, ans):
    if i < 0:
        return
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(heap):
        if heap[left] < heap[i]:
            smallest = left
    else:
        smallest = i
    if right < len(heap):
        if heap[right] < heap[smallest]:
            smallest = right
    if smallest != i:
        ans.append([heap[i], heap[smallest]])
        heap[i], heap[smallest] = heap[smallest], heap[i]
        return min_heapify(smallest, heap, ans)

def build_min_heap(to_heap):
    ans = []
    size = len(to_heap)
    for i in range(size // 2, -1, -1):
        min_heapify(i, to_heap, ans)
    print(len(ans))
    for pair in ans:
        print(pair[0], pair[1])
    return to_heap

line = '18 34 4 5 2 74 9 7 6 8 19'
to_heap = line.split(' ')
for i in range(len(to_heap)):
    to_heap[i] = int(to_heap[i])

print(build_min_heap(to_heap))