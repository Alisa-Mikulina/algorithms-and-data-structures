import time
t_start = time.perf_counter()

def intuitive_sorting(massive, length, indexes):
    for i in range(length):
        counter = i
        while massive[i] < massive[counter-1]:
            counter = counter - 1
        massive.insert(max(counter,0), massive[i])
        indexes.append(max(counter,0) + 1)
        massive.pop(i + 1)
    return [indexes, massive]

f = open("input.txt", "r")
length = int(f.readline())
massive = list(map(int, f.readline().split(" ")))
indexes = []
f.close()


d = open("output.txt", "w")
ans = intuitive_sorting(massive, length, indexes)
d.write(" ".join(map(str, ans[0])) + '\n' + " ".join(map(str, ans[1])))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))