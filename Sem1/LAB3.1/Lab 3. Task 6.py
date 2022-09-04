import time
t_start = time.perf_counter()

import random

def integer_sort(arr_1, arr_2):
    multiplied_array = []
    len_1 = len(arr_1)
    len_2 = len(arr_2)
    for i in range(len_1):
        for j in range(len_2):
            multiplied_array.append(arr_1[i] * arr_2[j])
    sorted_array = quick_sort(multiplied_array)
    print(sorted_array)
    ans = 0
    for i in range(0, len(sorted_array), 10):
        ans += sorted_array[i]
    return ans

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


with open("input.txt", "r") as f:
    len_1, len_2 = list(map(int, f.readline().split(" ")))
    array_1 = list(map(int, f.readline().split(" ")))
    array_2 = list(map(int, f.readline().split(" ")))

with open("output.txt", "w") as d:
    d.write(str(integer_sort(array_1, array_2)))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))