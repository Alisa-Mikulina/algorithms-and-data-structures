def min_dots(lines):
    open_close = []
    # 0 = open
    # 1 = close
    for i in range(len(lines)):
        open_close.append((lines[i][0], 0))
        open_close.append((lines[i][1], 1))
    open_close = sorted(open_close)
    dots = []
    for i in range(len(open_close) - 1):
        action = open_close[i][1]
        dot_next = open_close[i + 1][0]
        action_next = open_close[i + 1][1]
        if action == 0 and action_next == 1:
            dots.append(dot_next)
    return dots




with open('input_4.txt') as f:
    num_lines = int(f.readline())
    lines = []
    for i in range(num_lines):
        new_line = list(map(int, f.readline().split()))
        lines.append((new_line[0], new_line[1]))

ans = min_dots(lines)
print(len(ans))
print(' '.join(str(x) for x in ans))