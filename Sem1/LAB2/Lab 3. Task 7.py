import time
t_start = time.perf_counter()

def maximum_array(array):
    max_sum = array[0]
    current_sum = 0
    for i in array:
        current_sum += i
        if current_sum < 0:
            current_sum = 0
        max_sum = current_sum if max_sum < current_sum else max_sum
    return max_sum

with open("input.txt", "r") as f:
    length = int(f.readline())
    array = list(map(int, f.readline().split(" ")))

with open("output.txt", "w") as file:
    maximum = maximum_array(array)
    file.write(str(maximum))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))