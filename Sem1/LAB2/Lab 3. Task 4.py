import time
t_start = time.perf_counter()

def binary_search(array, to_find):
    start = 0
    end = len(array)
    while end - start != 1:
        middle = start + (end - start) // 2
        if to_find < array[middle]:
            end = middle
        else:
            start = middle
    if to_find == array[start]:
        return start
    else:
        return -1

with open("input.txt", "r") as f:
    length = int(f.readline())
    array = list(map(int, f.readline().split(" ")))
    to_find_num = int(f.readline())
    to_find = list(map(int, f.readline().split(" ")))

with open("output.txt", "w") as file:
    for i in range(to_find_num):
        found = binary_search(array, to_find[i])
        file.write(str(found) + ' ')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))