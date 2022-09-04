def phone_numbers(count):
    steps = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [9, 3, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}
    numbers = [[0 for i in range(10)] for j in range(count + 1)]
    for i in range(10):
        if i == 0 or i == 8:
            numbers[0][i] = 0
        else:
            numbers[0][i] = 1
    for i in range(count):
        for j in range(10):
            for k in steps[j]:
                numbers[i + 1][k] += numbers[i][j]
    return sum(numbers[-2])



n = int(input())
ans = phone_numbers(n)
print(ans)