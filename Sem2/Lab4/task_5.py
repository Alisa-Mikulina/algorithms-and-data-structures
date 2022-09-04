import time
t_start = time.perf_counter()

def prefix(line):
    stripped_line = list(line)
    len_line = len(line)
    pref = [0 for i in range(len_line)]
    j = 0

    for i in range(2, len_line + 1):
        while j > 0 and stripped_line[j] != stripped_line[i - 1]:
            j = pref[j - 1]
        if stripped_line[j] == stripped_line[i - 1]:
            j += 1
        pref[i - 1] = j

    return pref




with open('input_5.txt') as f:
    line = f.readline().strip()
    
ans = prefix(line)

with open('output_5.txt', 'w') as d:
    for elem in ans:
        d.write(str(elem) + ' ')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))