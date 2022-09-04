import time
t_start = time.perf_counter()

def radix_sort(line, num_lines, len_lines, num_phases):
    current_phase = 0
    for i in range(len_lines - 1, -1, -1):
        for p in range(0, num_lines - 1):
            if line[i][p] > line[i][p + 1]:
                for q in range(0, len_lines + 1):
                    line[q][p], line[q][p + 1] = line[q][p + 1], line[q][p]
        current_phase += 1
        if current_phase == num_phases:
            return line[-1]
    return line[-1]


lines = []
with open("input.txt", "r") as f:
    num_lines, len_lines, num_phases = list(map(int, f.readline().split(" ")))
    for i in range(len_lines):
        lines.append(list(f.readline()))

print(lines, num_lines, len_lines, num_phases)

for i in range(len_lines - 1):
    lines[i].pop()


print(lines, num_lines, len_lines, num_phases)

with open("output.txt", "w") as d:
    d.write(' '.join(list(map(str, radix_sort(lines, num_lines, len_lines, num_phases)))))


print("Время работы: %s секунд " % (time.perf_counter() - t_start))