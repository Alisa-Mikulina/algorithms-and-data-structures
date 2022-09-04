def min_heapify(heap, heap_size, i):
    if i < 0:
        return
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < heap_size:
        if heap[left] < heap[i]:
            smallest = left
    else:
        smallest = i
    if right < heap_size:
        if heap[right] < heap[smallest]:
            smallest = right
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        return min_heapify(heap, heap_size, smallest)

def build_min_heap(to_heap):
    heap_size = len(to_heap)
    for i in range(heap_size, -1, -1):
        min_heapify(to_heap, heap_size, i)
    return to_heap

def heap_sort(array):
    heap_size = len(array)
    array = build_min_heap(array)
    for i in range(heap_size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        min_heapify(array, i, 0)
    return array


line = '18 34 4 5 2 74 9 7 6 8 19'
array = line.split(' ')
for i in range(len(array)):
    array[i] = int(array[i])

print(heap_sort(array))