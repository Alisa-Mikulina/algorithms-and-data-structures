import time
t_start = time.perf_counter()

f = open("input.txt", "r")
massive = [int(a) for a in f.readline().split(" ")]
element = int(f.readline())
f.close()


countiterations = [0]
iterations = []
for i in range(len(massive)):
    if massive[i] == element:
        countiterations[0] += 1
        iterations.append(i+1)
if countiterations[0] == 0:
    ans = -1
elif countiterations[0] == 1:
    ans = iterations[0]
else:
    ans = [countiterations, iterations]



d = open("output.txt", "w")
if countiterations[0] > 1:
    d.write(" ".join(map(str, ans[0])) + ', ' + (", ".join(map(str, ans[1]))))
else:
    d.write(str(ans))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))