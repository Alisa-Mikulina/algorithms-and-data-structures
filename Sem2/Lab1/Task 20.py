def count_palindromes(length, max_diff, line):
    letters = []
    for letter in line:
        letters.append(letter)
    samples = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        cur_line = ''
        for j in range(length - i):
            cur_line = cur_line + letters[j]
            if cur_line == cur_line[::-1]:
                samples[i][j] = 1
            len_curline = len(cur_line)
            if len_curline % 2 == 0:
                half_len = len_curline // 2
                first = cur_line[:half_len]
                second = cur_line[half_len:]
                second = second[::-1]
                diff = 0
                for p in range(half_len):
                    if first[p] != second[p]:
                        diff += 1
                if diff <= max_diff:
                    samples[j][i] = 1
            else:
                half_len = len_curline // 2
                first = cur_line[:half_len + 1]
                second = cur_line[half_len - 1:]
                second = second[::-1]
                diff = 0
                for n in range(half_len):
                    if first[n] != second[n]:
                        diff += 1
                if diff <= max_diff:
                    samples[j][i] = 1
    counter = 0
    for i in range(length):
        for j in range(length):
            if samples[i][j] == 1:
                counter += 1


    return samples, counter



with open('input_20.txt') as f:
    length, max_diff = list(map(int, list(f.readline().split())))
    line = f.readline()

ans = count_palindromes(length, max_diff, line)
print(ans)

with open('output.txt', 'w') as d:
    d.write(str(ans))