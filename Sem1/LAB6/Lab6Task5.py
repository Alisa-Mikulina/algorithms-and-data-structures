import time
t_start = time.perf_counter()

class Election():
    def __init__(self):
        self.names = {}

    def add(self, name, votes):
        if name in self.names:
            self.names[name] += votes
            return
        self.names[name] = votes
        return

    def output(self):
        ans = ''
        for name in sorted(list(self.names.keys())):
            ans += str(name) + ' ' + str(self.names[name]) + '\n'
        return ans


set = Election()
ans = ''

with open("input_5.txt", "r") as f:
    for line in f.readlines():
        file = line.strip().split(' ')
        name, votes = file[0], int(file[1])
        set.add(name, votes)


with open("output_5.txt", "w") as d:
    d.write(set.output())


print("Время работы: %s секунд " % (time.perf_counter() - t_start))