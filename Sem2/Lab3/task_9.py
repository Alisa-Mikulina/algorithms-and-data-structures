class Graph:
    def __init__(self, num_nodes=0):
        self.dict_nodes = dict()
        self.num_nodes = num_nodes
        for i in range(num_nodes):
            self.dict_nodes[i + 1] = set()

    def add(self, first, second, cost):
        self.dict_nodes[first].add((second, cost))

    def find_cycles(self):
        def find(a=1, sumc=0):
            path = self.dict_nodes[a]
            color[a] = ('gray', sumc)
            for i in path:
                if color[i[0]][0] == 'gray':
                    if sumc + i[1] - color[i[0]][1] < 0:
                        nonlocal flag
                        flag = True
                elif color[i[0]][0] == 'white':
                    find(i[0], sumc + i[1])
            color[a] = ('black', sumc)
            nonlocal ready
            ready.discard(a)

        color = dict()
        ready = set()
        flag = False
        for i in range(self.num_nodes):
            color[i + 1] = ('white', 0)
            ready.add(i + 1)

        while ready:
            find(ready.pop())

        return flag


with open('input_9.txt') as f:
    num_nodes, num_connections = list(map(int, f.readline().split()))
    g = Graph(num_nodes)
    for i in range(num_connections):
        first, second, cost = list(map(int, f.readline().split()))
        g.add(first, second, cost)


print(int(g.find_cycles()))