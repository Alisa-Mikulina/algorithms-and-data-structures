import time
t_start = time.perf_counter()

class Phonebook():
    def __init__(self):
        self.items = {}

    def add(self, number, name):
        if name == 'not found':
            raise AssertionError('Wrong Name!')
        self.items[number] = name

    def find(self, number):
        name = self.items.get(number)
        if name == None:
            return 'not found'
        else:
            return name

    def delete(self, number):
        if self.items.get(number) != None:
            del self.items[number]
        return

    def output(self):
        return self.items


book = Phonebook()
ans = []

with open("input_2.txt", "r") as f:
    num_actions = int(f.readline())
    for i in range(num_actions):
        file = f.readline().strip().split(' ')
        if len(file) > 2:
            number, name = int(file[1]), file[2]
            book.add(number, name)
        else:
            if file[0] == 'del':
                number = int(file[1])
                book.delete(number)
            else:
                number = int(file[1])
                ans.append(book.find(number))

with open("output_2.txt", "w") as d:
    for answer in ans:
        d.write(answer + '\n')


print("Время работы: %s секунд " % (time.perf_counter() - t_start))