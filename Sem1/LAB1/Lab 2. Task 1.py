import time
t_start = time.perf_counter()

def intuitive_sorting(massive, length):
    for i in range(length):
        counter = i
        while massive[i] < massive[counter-1]:
            counter = counter - 1
        massive.insert(max(counter,0), massive[i])
        massive.pop(i + 1)
    return massive

f = open("input.txt", "r")
length = int(f.readline())
massive = list(map(int, f.readline().split(" ")))
f.close()

d = open("output.txt", "w")
d.write(' '.join(list(map(str,intuitive_sorting(massive, length)))))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))