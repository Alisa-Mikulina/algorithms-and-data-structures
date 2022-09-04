from operator import length_hint
from numpy import Inf


def find_route(distances, cities, maximum):
    length_way = [Inf, []]
    cities_ids = [x for x in range(len(distances[0]))]
    ways = [[[[] for k in range(maximum * cities)] for j in range(cities)] for i in range(cities + 1)]
    for id in cities_ids:
        for k in range(cities):
            if (id != k) and (k not in ways[0][k][distances[id][k]]) and (id not in ways[0][k][distances[id][k]]):
                ways[0][k][distances[id][k]].append(id)
                ways[0][k][distances[id][k]].append(k)
                #print(ways[0][k][distances[id][k]])
    for i in range(cities):
        for j in range(cities):
            for k in range(maximum * cities):
                if len(ways[i][j][k]) != 0:
                    curr_way = ways[i][j][k]
                    print(curr_way, i)
                    for id in cities_ids:
                        if id not in curr_way:
                            ways[i + 1][id][k + distances[j][id]] += curr_way
                            ways[i + 1][id][k + distances[j][id]].append(id)
                        # if i == cities - 2:
                        #     if k + distances[j][id] < length_way[0]:
                        #         length_way[0] = k + distances[j][id]
                        #         print(i, j, k)
                        #         print(k + distances[j][id], ways[i + 1][id][k + distances[j][id]])
                        #         length_way[1] = ways[i + 1][id][k + distances[j][id]]
    
    i = cities - 2
    for j in range(cities):
        for k in range(maximum * cities):
            # print(ways[i][j][k])
            if k < length_way[0] and len(ways[i][j][k]) != 0:
                # print(k)
                length_way[0] = k
                length_way[1] = ways[i][j][k]
    for i in range(len(length_way[1])):
        length_way[1][i] += 1
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
print(ans)