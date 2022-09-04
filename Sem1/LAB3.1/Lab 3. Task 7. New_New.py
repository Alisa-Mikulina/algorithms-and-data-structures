import random
import time
t_start = time.perf_counter()


def indexes(arr):
    return list(map(lambda x: x[-1] + 1, arr))


def radix_sort(arr, phases_count):
    string_len = len(lines[0]) - 1
    for i in range(min(phases_count, string_len)):
        quick_sort(arr, string_len - i - 1)

    return indexes(arr)


def quick_sort(array, index):
    if len(array) == 0:
        return array
    length = len(array)
    separator_start = random.randint(index, length - 1)
    separator_elem = array[separator_start][index]
    smaller, bigger, separator = [], [], []
    for i in range(0, length):
        if array[i][index] < separator_elem:
            smaller.append(array[i])
        elif array[i][index] == separator_elem:
            separator.append(array[i])
        else:
            bigger.append(array[i])
    return [*quick_sort(smaller, index), *separator, *quick_sort(bigger, index)]


with open("input.txt", "r") as f:
    num_lines, len_lines, num_phases = list(map(int, f.readline().split(" ")))
    lines = [[] for i in range(num_lines)]
    for i in range(len_lines):
        chars = list(f.readline())
        for j in range(len(chars)):
            if chars[j] != "\n":
                lines[j].append(chars[j])
    for i in range(num_lines):
        lines[i].append(i)

with open("output.txt", "w") as d:
    d.write(' '.join(list(map(str, radix_sort(lines, num_phases)))))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
