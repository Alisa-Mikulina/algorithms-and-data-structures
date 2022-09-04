import time
t_start = time.perf_counter()

import random

def quick_sort(array):
    if len(array) == 0:
        return array
    length = len(array)
    separator_start = random.randint(0, length - 1)
    separator_elem = array[separator_start]
    smaller, bigger, separator = [], [], []
    for i in range(0, length):
        if array[i] < separator_elem:
            smaller.append(array[i])
        elif array[i] == separator_elem:
            separator.append(array[i])
        else:
            bigger.append(array[i])
    return [*quick_sort(smaller), *separator, *quick_sort(bigger)]

f = open("input.txt", "r")
length = int(f.readline())
array = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(' '.join(list(map(str,quick_sort(array)))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))