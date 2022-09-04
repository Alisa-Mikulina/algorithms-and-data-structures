import time
t_start = time.perf_counter()

def quick_sort(array):
    if len(array) > 1:
        length = len(array)
        middle = length // 2
        smaller, bigger = [], []
        middle_element = array[middle]
        for i in range(middle):
            if array[i] < middle_element:
                smaller.append(array[i])
            else:
                bigger.append(array[i])
        for j in range(middle + 1, length):
            if array[j] < middle_element:
                smaller.append(array[j])
            else:
                bigger.append(array[j])
        return [*quick_sort(smaller), middle_element, *quick_sort(bigger)]
    else:
        return array

f = open("input", "r")
length = int(f.readline())
array = list(map(int, f.readline().split(" ")))
f.close()

d = open("output", "w")
d.write(' '.join(list(map(str,quick_sort(array)))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))