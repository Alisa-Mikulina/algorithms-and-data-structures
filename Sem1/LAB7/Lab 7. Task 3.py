import time
t_start = time.perf_counter()


def editing_distance(word1, word2, top, side):
    matrix = [[None for i in range(top + 1)] for j in range(side + 1)]
    for i in range(side + 1):
        for j in range(top + 1):
            if i == 0 or j == 0:
                matrix[i][j] = i + j
                continue
            difference = 0 if word2[i - 1] == word1[j - 1] else 1
            matrix[i][j] = min(matrix[i - 1][j - 1] + difference, matrix[i - 1][j] + 1, matrix[i][j - 1] + 1)
    return matrix[side][top]


with open("input_3.txt", "r") as f:
    string_1 = f.readline().strip().split(' ')
    string_2 = f.readline().split(' ')

string_1[0] = string_1[0]
string_2[0] = string_2[0]
word1 = string_1[0]
word2 = string_2[0]
string_1 = []
string_2 = []
for char in word1:
    string_1.append(char)
for char in word2:
    string_2.append(char)
top = len(string_1)
side = len(string_2)

ans = editing_distance(string_1, string_2, top, side)
print(ans)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))