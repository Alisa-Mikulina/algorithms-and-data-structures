import math
import random
import time
t_start = time.perf_counter()

def find_K_dots(coordinates, K):
    for dot in coordinates:
        distance = math.sqrt((dot[0] ** 2) + (dot[1] ** 2))
        dot.insert(0, distance)
    sorted_dots = quick_sort(coordinates)
    ans = ''
    for i in range(1, K + 1):
        ans += "[" + str(sorted_dots[i - 1][1]) + "," + str(sorted_dots[i - 1][2]) + "]"
        if i < K:
            ans += ","
    return ans


def quick_sort(array):
    if len(array) == 0:
        return array
    length = len(array)
    separator_start = random.randint(0, length - 1)
    separator_elem = array[separator_start][0]
    smaller, bigger, separator = [], [], []
    for i in range(0, length):
        if array[i][0] < separator_elem:
            smaller.append(array[i])
        elif array[i][0] == separator_elem:
            separator.append(array[i])
        else:
            bigger.append(array[i])
    return [*quick_sort(smaller), *separator, *quick_sort(bigger)]



coordinates = []
with open("input.txt", "r") as f:
    num, K = list(map(int, f.readline().split(" ")))
    for i in range(num):
        x, y = list(map(int, f.readline().split(" ")))
        coordinates. append([x, y])

with open("output.txt", "w") as d:
    d.write(find_K_dots(coordinates, K))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))