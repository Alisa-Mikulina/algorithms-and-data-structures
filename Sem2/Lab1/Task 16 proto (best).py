from numpy import Inf


def find_route(distances, cities, maximum):
    length_way = [Inf, []]
    max_possible = 2 ** cities - 1
    ways = [[[Inf, Inf] for j in range(max_possible + 1)] for i in range(cities)]
    for i in range(cities):
        path = 2 ** i
        ways[0][path] = [0, i]

    for i in range(cities):
        for k in range(max_possible + 1):
            if ways[i][k][0] != Inf:
                for j in range(cities):
                    if (k & (2 ** j)) == 0 and (k + 2 ** j) <= max_possible:
                        current = ways[i + 1][k + 2 ** j][0]
                        new = ways[i][k][0] + distances[ways[i][k][1]][j]
                        if current > new:
                            ways[i + 1][k + 2 ** j][0] = new
                            ways[i + 1][k + 2 ** j][1] = j

    length_way[0] = ways[cities - 1][max_possible][0]
    way = []
    way.append(ways[cities - 1][max_possible][1])
    j = max_possible
    for i in range(cities - 1, 0, -1):
        j = j - 2 ** way[-1]
        to_add = ways[i - 1][j][1]
        way.append(to_add)
    
    for i in range(len(way)):
        way[i] = way[i] + 1

    length_way[1] = way
    
    return length_way




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
print(ans[0])
print(ans[1])