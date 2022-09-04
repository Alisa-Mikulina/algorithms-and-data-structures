import time
t_start = time.perf_counter()

def choice_sorting(massive, length):
    minimum = massive[0]
    for j in range(length):
        minimum = massive[j]
        for i in range(j, length):
            if minimum > massive[i]:
                minimum, massive[i] = massive[i], minimum
        massive[j] = minimum
    return massive

f = open("input.txt", "r")
length = int(f.readline())
massive = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(' '.join(list(map(str,choice_sorting(massive, length)))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))