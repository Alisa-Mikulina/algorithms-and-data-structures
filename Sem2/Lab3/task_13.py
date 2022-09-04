class Garden:
    def __init__(self) -> None:
        self.height = 0
        self.length = 0
        self.grid = []
        self.beds = 0
        self.visited = []

    
    def count_beds(self):
        self.visited = [[False for i in range(self.length)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.length):
                if self.grid[i][j] == '#':
                    self.beds += 1
                    self.visited[i][j] = True
                    self.discover_bed(i, j, self.beds)
        return self.beds
    

    def discover_bed(self, x, y, id):
        this_cluster = [[x, y]]
        possible_routes = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        while this_cluster != []:
            x, y = this_cluster[-1]
            this_cluster.pop()
            for pair in possible_routes:
                m, p = x + pair[0], y + pair[1]
                if (0 <= m < self.height) and (0 <= p < self.length):
                    if self.visited[m][p] == True:
                        continue
                    elif self.grid[m][p] == '#':
                        self.visited[m][p] = True
                        this_cluster.append([m, p])
            self.grid[x][y] = str(id)
        return




with open('input.txt') as f:
    height, length = list(map(int, f.readline().split()))
    grid = []
    for i in range(height):
        gridline = []
        new_line = list(f.readline().strip())
        grid.append(new_line)

g = Garden()
g.height = height
g.length = length
g.grid = grid

ans = g.count_beds()

with open('output.txt', 'w') as d:
    d.write(str(ans))