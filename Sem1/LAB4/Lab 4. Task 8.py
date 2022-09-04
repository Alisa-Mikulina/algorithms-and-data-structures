import time
t_start = time.perf_counter()

def counter(expression, elements, stack):
    for i in range(elements):
        if expression[i] != '-' and expression[i] != '+' and expression[i] != '*':
            stack.append(expression[i])
        else:
            operation = expression[i]
            b = stack.pop()
            a = stack.pop()
            if operation == '-':
                stack.append(a - b)
            elif operation == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)


stack = []

with open("input.txt", "r") as f:
    elements = int(f.readline())
    expression = list(f.readline().split(' '))
    for i in range(elements):
        if expression[i] != '-' and expression[i] != '+' and expression[i] != '*':
            expression[i] = int(expression[i])
    counter(expression, elements, stack)


with open("output.txt", "w") as d:
    d.write(str(stack[0]))

print("Время работы: %s секунд " % (time.perf_counter() - t_start))