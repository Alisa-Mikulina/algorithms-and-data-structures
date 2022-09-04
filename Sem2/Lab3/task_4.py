def linear(connections, num_nodes):
    line = []
    for key in connections.keys():
        line = go_deep(connections, key, line)
        if key not in line:
            line.append(key)
    for i in range(len(line)):
        line[i] += 1
    return line[::-1]


def go_deep(connections, node, line):
    if connections[node] != []:
        children = connections[node]
    else:
        if node not in line:
            line.append(node)
        return line
    for child in children:
        line = go_deep(connections, child, line)
        if child not in line:
            line.append(child)
    return line


with open('input_4.txt') as f:
    num_nodes, num_connections = list(map(int, f.readline().split()))
    connections = {}
    for i in range(num_nodes):
        connections[i] = []
    for i in range(num_connections):
        first, second = list(map(int, f.readline().split()))
        connections[first - 1].append(second - 1)
    print(connections)

print(linear(connections, num_nodes))