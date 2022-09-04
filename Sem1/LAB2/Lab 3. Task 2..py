import time
t_start = time.perf_counter()


def merge_sorting(arr, start, end, file):
    if start < end:
        middle = (start + end) // 2
        merge_sorting(arr, start, middle, file)
        merge_sorting(arr, middle + 1, end, file)
        merge(arr, start, end, file)
        return arr
    else:
        return arr


def merge(arr, start, end, file):
    middle = (start + end) // 2
    left_array, right_array = arr[start:middle + 1:], arr[middle + 1:end + 1:]
    count_left, count_right = 0, 0
    for i in range(start, end + 1):
        if find_elem(left_array, count_left) < find_elem(right_array, count_right):
            arr[i] = left_array[count_left]
            count_left += 1
        else:
            arr[i] = right_array[count_right]
            count_right += 1
    file.write(f'{start + 1} {end + 1} {arr[start]} {arr[end]} \n')
    return arr


def find_elem(arr, index):
    if index < len(arr):
        return arr[index]
    else:
        return 10 ** 10


def sort(arr, file):
    return merge_sorting(arr, 0, len(array) - 1, file)


with open("input.txt", "r") as f:
    length = int(f.readline())
    array = list(map(int, f.readline().split(" ")))

with open("output.txt", "w") as file:
    sorted = sort(array, file)
    file.write(' '.join(list(map(str, sorted))))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
