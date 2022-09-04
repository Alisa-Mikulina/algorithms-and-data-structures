import time
t_start = time.perf_counter()

def add(my_queue, number):
    global tail
    my_queue.append(number)
    tail += 1

def delete(my_queue, ans):
    global nose
    ans.append(my_queue[nose])
    nose += 1

my_queue = []
ans = []
nose, tail = 0, 1

with open("input.txt", "r") as f:
    iterations = int(f.readline())
    for i in range(iterations):
        line = f.readline().strip()
        if len(line) > 2:
            action, number = list(line.split(" "))
            add(my_queue, number)
        else:
            action = line
            delete(my_queue, ans)


with open("output.txt", "w") as d:
    for elem in ans:
        d.write(str(elem) + '\n')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))