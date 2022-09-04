def find_route(connections, c_one, c_two):
    if not c_one in connections or connections[c_one] == []:
        return 0
    if c_two in connections[c_one]:
        return 1
    else:
        children = connections[c_one]
        for child in children:
            ans = find_route(connections, child, c_two)
            if ans == 1:
                return 1
    return 0




with open('input_1.txt') as f:
    num_nodes, num_connections = list(map(int, f.readline().split()))
    connections = {}
    for i in range(num_nodes):
        connections[i] = []
    for i in range(num_connections):
        first, second = list(map(int, f.readline().split()))
        connections[first - 1].append(second - 1)
    print(connections)
    c_one, c_two = list(map(int, f.readline().split()))

whether_found = find_route(connections, c_one - 1, c_two - 1)

print(whether_found)