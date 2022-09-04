import time
t_start = time.perf_counter()

def merge_sorting(array, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sorting(array, start, middle)
        merge_sorting(array, middle+1, end)
        return merge(array, start, middle, end)
    else:
        return True

def merge(arr, start, middle, end):
    left_array, right_array = arr[start:middle + 1:], arr[middle + 1:end + 1:]
    count_left, count_right = 0, 0
    maximum = 0
    current = 0
    for i in range(start, end + 1):
        if find_elem(left_array, count_left) < find_elem(right_array, count_right):
            arr[i] = left_array[count_left]
            count_left += 1
        else:
            arr[i] = right_array[count_right]
            count_right += 1
        if i == start or arr[i] == arr[i - 1]:
            current += 1
        else:
            maximum = current if current > maximum else maximum
            current = 1
    return maximum > len(arr) / 2

def find_elem(ar, index):
    if index < len(ar):
        return ar[index]
    else:
        return 10**10

def sort(array):
    return merge_sorting(array, 0, len(array) - 1)

f = open("input.txt", "r")
length = int(f.readline())
array = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(str(int(sort(array))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))