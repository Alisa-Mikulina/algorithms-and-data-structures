def find_cycles(connections, num_nodes):
    colours = ['white' for i in range(num_nodes)]
    for i in range(num_nodes):
        if colours[i] == 'white':
            try:
                new = connections[i][0]
                colours[i] = 'grey'
                trial = explore(connections, colours, new)
                if trial != 1:
                    colours[new] = 'black'
                else:
                    return 1
            except:
                continue
    return 0
        


def explore(connections, colours, host):
    if len(connections[host]) == 0:
        return
    children = connections[host]
    for child in children:
        if colours[child] == 'grey':
            return 1
        elif colours[child] == 'black':
            return
        else:
            new_host = child
            colours[new_host] = 'grey'
            trial = explore(connections, colours, new_host)
            if trial != 1:
                colours[new_host] = 'black'
                return
            else:
                return 1



with open('input_3.txt') as f:
    num_nodes, num_connections = list(map(int, f.readline().split()))
    connections = {}
    for i in range(num_nodes):
        connections[i] = []
    for i in range(num_connections):
        first, second = list(map(int, f.readline().split()))
        connections[first - 1].append(second - 1)

print(find_cycles(connections, num_nodes))