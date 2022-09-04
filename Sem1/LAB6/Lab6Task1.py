import time
t_start = time.perf_counter()

class MySet():
    def __init__(self, size):
        self.size = size
        self.myset = [[] for p in range(size)]
    
    def find(self, x):
        for now in self.myset[x % self.size]:
            if now == x:
                return 'Y'
        return 'N'
    
    def add(self, x):
        if self.find(x) == 'Y':
            return
        self.myset[x % self.size].append(x)

    def delete(self, x):
        xlist = self.myset[x % self.size]
        for i in range(len(xlist)):
            if xlist[i] == x:
                xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
                xlist.pop()
                return self.myset
        return self.myset


set = MySet(5 * (10 ** 5))
ans = []

with open("input.txt", "r") as f:
    num_actions = int(f.readline())
    for i in range(num_actions):
        action, number = f.readline().split(' ')
        number = int(number)
        if action == 'A':
            set.add(number)
        elif action == 'D':
            set.delete(number)
        elif action == '?':
            ans.append(set.find(number))

with open("output.txt", "w") as d:
    for answer in ans:
        d.write(answer + '\n')


print("Время работы: %s секунд " % (time.perf_counter() - t_start))