# import time
# t_start = time.perf_counter()


def zed(line):
  zedded = [0] * len(line)
  L, R = 0, 0
  for i in range(1, len(line)):
    zedded[i] = max(0, min(zedded[i - L], R - i))
    while i + zedded[i] < len(line) and line[zedded[i]] == line[i + zedded[i]]:
      zedded[i] += 1
    if i + zedded[i] > R:
      L, R = i, i + zedded[i]
  return zedded



with open('input_6.txt') as f:
    line = f.readline().strip()
    
ans = zed(line)[1:]

with open('output_6.txt', 'w') as d:
    for elem in ans:
        d.write(str(elem) + ' ')

# print("Время работы: %s секунд " % (time.perf_counter() - t_start))