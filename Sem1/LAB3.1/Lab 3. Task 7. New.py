import time
t_start = time.perf_counter()


def indexes(arr):
    ans = []
    current_ans = 0
    for i in arr:
        current_ans = i[-1] + 1
        ans.append(current_ans)
    return ans


def radix_sort(arr, phases_count):
    string_len = len(lines[0]) - 1
    initial_arr = arr[::]
    for i in range(min(phases_count, string_len)):
        count_sort(arr, string_len - i - 1, initial_arr)

    return indexes(arr)


def count_sort(array, i, initial_arr):
    start = ord('a')
    end = ord('z')
    count = [[] for _ in range(start, end + 1)]
    for string in array:
        count[ord(string[i]) - start].append(string[-1])

    temp = []
    current = 0
    for i in range(0, len(count)):
        for t in range(len(count[i])):
            add = initial_arr[count[i][t]]
            temp.append(add)
            current += 1
    for i in range(len(array)):
        array[i] = temp[i]


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
