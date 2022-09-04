def find_three(line):
    count = 0
    first = ord('a')
    last = ord('z')
    full = []
    left = []
    for i in range(first, last + 1):
        full.append(0)
        left.append(0)
    for char in line:
        id_ = ord(char)
        full[id_ - first] += 1
    for char in line:
        id_ = ord(char) - first
        left[id_] += 1
        for i in range(len(full)):
            if i == id_:
                right = full[i] - left[i]
                cur_left = left[i] - 1
                count += cur_left * right
            else:
                right = full[i] - left[i]
                count += left[i] * right
    return count




with open('input.txt') as f:
    line = f.readline().split()
    text = ''
    for word in line:
        text += word

ans = find_three(text)

with open('output.txt', 'w') as d:
    d.write(str(ans))