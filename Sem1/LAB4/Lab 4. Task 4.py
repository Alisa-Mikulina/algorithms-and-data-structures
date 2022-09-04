import time
t_start = time.perf_counter()

def is_correct(line):
    stack = []
    equals_back = {')': '(', ']': '[', '}': '{'}
    for i in range(0, len(line)):
        if line[i] not in ['(', ')', '[', ']', '{', '}']:
            continue
        if line[i] in equals_back.values():
            stack.append([line[i], i])
        else:
            if stack:
                if stack[-1][0] == equals_back[line[i]]:
                    stack.pop()
                else:
                    stack.append([line[i], i])
                    for p in range(len(stack) - 1, -1, -1):
                        if stack[p][0] in equals_back.keys():
                            return str(stack[p][-1] + 1)
                    return str(stack[0][-1] + 1)
            else:
                return str(i + 1)
    if not stack:
        return 'Success'
    else:
        return str(stack[0][-1] + 1)


with open("input.txt", "r") as f:
    line = f.readline().split()
    ans = is_correct(line[0])

with open("output.txt", "w") as d:
    d.write(ans)

print("Время работы: %s секунд " % (time.perf_counter() - t_start))
