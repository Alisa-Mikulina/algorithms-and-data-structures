def check_level(i, heap):
    left = 2 * i
    right = 2 * i + 1
    if left < len(heap):
        if not heap[left] >= heap[i]:
            return False
    if right < len(heap):
        if not heap[right] >= heap[i]:
            return False
    return True

heap = input().split(' ')
for i in range(len(heap)):
    heap[i] = int(heap[i])
heap.insert(0, -1)
ans = "YES"

for i in range(len(heap)):
    if check_level(i, heap):
        continue
    else:
        ans = "NO"
        break
print(ans)