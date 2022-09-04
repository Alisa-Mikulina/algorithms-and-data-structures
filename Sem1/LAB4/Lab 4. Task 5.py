import time
t_start = time.perf_counter()

def add(number, stack):
    current_maximum = max(number, stack[0][0])
    stack[0][0] = current_maximum
    stack.append([number, current_maximum])

def delete(stack):
    stack.pop()
    stack[0][0] = stack[-1][-1]

def stack_max(stack):
    global ans
    ans.append(stack[-1][-1])

stack = [[-1]]
ans = []

with open("input.txt", "r") as f:
    iterations = int(f.readline())
    for i in range(iterations):
        line = list(f.readline().splitlines())
        line = list(line[0].split(' '))
        if len(line) > 1:
            number = int(line[-1])
            add(number, stack)
        else:
            action = line[0]
            if action == 'pop':
                delete(stack)
            else:
                stack_max(stack)


with open("output.txt", "w") as d:
    for elem in ans:
        d.write(str(elem) + '\n')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))