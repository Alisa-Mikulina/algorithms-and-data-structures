class Graph():
    def __init__(self) -> None:
        self.instructions = {}
        self.i_have = ''
        self.i_want = ''
        self.used = []

    def find_my(self):
        if self.i_have == self.i_want:
            return 0
        else:
            if self.i_have not in self.instructions:
                return -1
            self.used.append(self.i_have)
            self.i_have = self.instructions[self.i_have]
            if self.i_want in self.i_have:
                return 1
            ans = self.go_deep(step=1)
        return ans


    def go_deep(self, step):
        if self.i_have == []:
            return - 1
        next_step = []
        for elem in self.i_have:
            if elem in self.instructions:
                self.used.append(elem)
                potential = self.instructions[elem]
                for pot in potential:
                    if (pot not in next_step) and (pot not in self.used):
                        next_step.append(pot)
        if self.i_want in next_step:
            return step + 1
        else:
            self.i_have = next_step
            next_step = []
            steps = self.go_deep(step + 1)
            return steps



with open('input.txt') as f:
    num = int(f.readline())
    instructions = {}
    for i in range(num):
        lst = f.readline().split()
        first, second = lst[0], lst[2]
        if first not in instructions:
            instructions[first] = [second]
        else:
            instructions[first].append(second)
    i_have = f.readline().split()[0]
    i_want = f.readline().split()[0]

gr = Graph()
gr.instructions = instructions
gr.i_have = i_have
gr.i_want = i_want

ans = (gr.find_my())
# print(ans)
with open('output.txt', 'w') as d:
    d.write(str(ans))