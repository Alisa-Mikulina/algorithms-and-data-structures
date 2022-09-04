import time
t_start = time.perf_counter()

def anti_quick_sort(array):
    for i in range(2, len(array)):
        array[i] = i + 1
        array[i // 2], array[i] = array[i], array[i // 2]
    return array

def quick_sort(array):
    global count_comparisons
    if len(array) > 1:
        length = len(array)
        middle = length // 2
        smaller, bigger = [], []
        middle_element = array[middle]
        for i in range(middle):
            if array[i] < middle_element:
                smaller.append(array[i])
                count_comparisons += 1
            else:
                bigger.append(array[i])
                count_comparisons += 1
        for j in range(middle + 1, length):
            if array[j] < middle_element:
                smaller.append(array[j])
                count_comparisons += 1
            else:
                bigger.append(array[j])
                count_comparisons += 1
        return [*quick_sort(smaller), middle_element, *quick_sort(bigger)]
    else:
        count_comparisons += 1
        return array


with open("input.txt", "r") as f:
    length = int(f.readline())

arr = [i for i in range(1, length + 1)]
count_comparisons = 0
anti_list = anti_quick_sort(arr)
print(quick_sort(anti_list))

with open("output.txt", "w") as d:
    d.write(' '.join(list(map(str,anti_list))))
    d.write('\n' + str(count_comparisons))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))