import time
t_start = time.perf_counter()

def anti_quick_sort(array):
    for i in range(2, len(array)):
        array[i // 2], array[i] = array[i], array[i // 2]
    return array

with open("input.txt", "r") as f:
    length = int(f.readline())

arr = [i for i in range(1, length + 1)]
anti_list = anti_quick_sort(arr)

with open("output.txt", "w") as d:
    d.write(' '.join(list(map(str,anti_list))))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))