def count_palindromes(length, max_diff, line):
    letters = []
    counter = 0
    for letter in line:
        letters.append(letter)
    samples = [[0 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            if length - j <= i:
                samples[i][j] = None
            elif i == 0:
                samples[i][j] = 0
                counter += 1
            elif i == 1:
                if letters[j] == letters[j + 1]:
                    samples[i][j] = 0
                    counter += 1
                else:
                    samples[i][j] = 1
                    if 1 <= max_diff:
                        counter += 1
            else:
                middle = samples[i - 2][j + 1]
                if letters[j] == letters[j + i]:
                    samples[i][j] = middle
                    if middle <= max_diff:
                        counter += 1
                else:
                    samples[i][j] = middle + 1
                    if middle + 1 <= max_diff:
                        counter += 1

    return counter



with open('input.txt') as f:
    length, max_diff = list(map(int, list(f.readline().split())))
    line = f.readline()

ans = count_palindromes(length, max_diff, line)
print(ans)

with open('output.txt', 'w') as d:
    d.write(str(ans))