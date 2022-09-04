from re import I
from numpy import Inf


def find_route(distances, cities, maximum):
    length_way = [Inf, []]
    max_possible = ''
    for i in range(cities):
        max_possible += '1'
    max_possible = int(max_possible, 2)
    ways = [[[Inf, 0] for j in range(max_possible + 1)] for i in range(cities + 1)]
    for j in range(cities):
        for k in range(cities):
            if j != k:
                adress = 2 ** j + 2 ** k
                current = ways[0][adress][0]
                if distances[j][k] < current:
                    ways[0][adress][0] = min(current, distances[j][k])
                    ways[0][adress][1] = k

    for i in range(cities):
        for k in range(max_possible):
            if ways[i][k][0] != Inf:
                for j in range(cities):
                    if (k & 2 ** j) == 0 and (k + 2 ** j) <= max_possible:
                        current = ways[i + 1][k + 2 ** j][0]
                        new = ways[i][k][0] + distances[ways[i][k][1]][j]
                        if current > new:
                            ways[i + 1][k + 2 ** j][0] = new
                            ways[i + 1][k + 2 ** j][1] = j


    return ways




with open ("input_16.txt") as f:
    cities = int(f.readline())
    distances  = []
    maximum = 0
    for i in range(cities):
        line = f.readline()
        line_split = list(map(int, line.split()))
        distances.append(line_split)
        if max(line_split) > maximum:
            maximum = max(line_split)

ans = find_route(distances, cities, maximum)
print(ans)

print(11 & 4)