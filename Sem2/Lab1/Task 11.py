def max_possible_value(max_value, num_ingots, ingots):
    ingots.append(0)
    ingots = sorted(ingots)
    weights = [[False for i in range(max_value + 1)] for j in range(num_ingots + 1)]
    weights[0][0] = True
    for i in range(1, num_ingots + 1):
        for j in range(max_value + 1):
            difference = j - ingots[i]
            if difference >= 0:
                if weights[i - 1][difference]:
                    weights[i][j] = True
            if weights[i - 1][j]:
                weights[i][j] = True
    ans = 0
    i = len(weights[0]) - 1
    while ans == 0 and i >= 0:
        if weights[-1][i] == True:
            ans = i 
        i -= 1
    return ans


with open('input_11.txt') as f:
    max_value, num_ingots = f.readline().split()
    max_value, num_ingots = int(max_value), int(num_ingots)
    ingots = f.readline().split()
    for i in range(num_ingots):
        ingots[i] = int(ingots[i])

# max_value, num_ingots = list(map(int, input().split(' ')))
# ingots = list(map(int, input().split(' '))) 
ans = max_possible_value(max_value, num_ingots, ingots)
print(ans)