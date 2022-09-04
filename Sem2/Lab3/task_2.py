def count_clusters(connections, num_nodes):
    visited = [0 for i in range(num_nodes)]
    clust_num = 0 
    for host in connections.keys():
        if not visited[host]:
            children = connections[host]
            explore(host, children, visited, connections)
            clust_num += 1
    return clust_num


def explore(host, children, visited, connections):
    visited[host] = 1
    for child in children:
        if not visited[child]:
            new_host = child
            new_children = connections[new_host]
            explore(new_host, new_children, visited, connections)
    return




with open('input_2.txt') as f:
    num_nodes, num_connections = list(map(int, f.readline().split()))
    connections = {}
    for i in range(num_nodes):
        connections[i] = []
    for i in range(num_connections):
        first, second = list(map(int, f.readline().split()))
        connections[first - 1].append(second - 1)
        connections[second - 1].append(first - 1)
    print(connections)

print(count_clusters(connections, num_nodes))