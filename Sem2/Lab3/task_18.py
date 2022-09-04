from math import inf

def build_graph(distances):
    length = 0
    united = set()
    isolated = {}
    sides = []
    for distance in distances:
        if (distance[1] not in united) or (distance[2] not in united):
            if (distance[1] not in united) and (distance[2] not in united):
                isolated[distance[1]] = [distance[1], distance[2]]
                isolated[distance[2]] = isolated[distance[1]]
            else:
                if not isolated.get(distance[1]):
                    isolated[distance[2]].append(distance[1])
                    isolated[distance[1]] = isolated[distance[2]]
                else:
                    isolated[distance[1]].append(distance[2])
                    isolated[distance[2]] = isolated[distance[1]]
            sides.append(distance)
            united.add(distance[1])
            united.add(distance[2])

    for distance in distances:
        if distance[2] not in isolated[distance[1]]:
            sides.append(distance)
            first_group = isolated[distance[1]]
            isolated[distance[1]] += isolated[distance[2]]
            isolated[distance[2]] += first_group
    
    for side in sides:
        length += side[0]
    
    return length


def calculate_distance(x1, y1, x2, y2):
    dist = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)
    return dist


def fill(distances, nodes, num_nodes):
    for i in range(num_nodes):
        for j in range(num_nodes):
            if j > i:
                continue
            elif i == j:
                continue
            else:
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]
                distance = calculate_distance(x1, y1, x2, y2)
                distances.append((distance, i, j))
    dist = sorted(distances, key=lambda x: x[0])
    return dist


with open('input_18.txt') as f:
    num_nodes = int(f.readline())
    nodes = {}
    for i in range(num_nodes):
        x, y = list(map(int, f.readline().split()))
        nodes[i] = [x, y] 
    distances = []
    distances = fill(distances, nodes, num_nodes)
    print(distances)

ans = build_graph(distances)
print(format(ans,".9f"))