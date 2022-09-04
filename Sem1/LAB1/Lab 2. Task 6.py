import time
t_start = time.perf_counter()

def bubble_sorting(massive, length):
    for i in range(length):
        for j in range(length - 1, i, -1):
            if massive[j] < massive[j - 1]:
                massive[j], massive[j - 1] = massive[j - 1], massive[j]
    return massive

f = open("input.txt", "r")
length = int(f.readline())
massive = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(' '.join(list(map(str,bubble_sorting(massive, length)))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))