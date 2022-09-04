import random

options = ['delete', 'get', 'prev', 'next', 'put']
actions = []
nums = []

for i in range(100000):
    to_add = random.randrange(0, 5)
    actions.append(options[to_add])

for i in range(100000):
    to_add = random.randrange(10, 99)
    to_add_2 = random.randrange(10, 99)
    if actions[i] == 'put':
        actions[i] = actions[i] + ' ' + str(to_add) + ' ' + str(to_add_2)
    else:
        actions[i] = actions[i] + ' ' + str(to_add)

# print(actions)
# print(nums)
# print(len(nums))

with open("input.txt", "w") as d:
    d.write(str(len(actions)) + '\n')
    for i in range(100000):
        d.write(actions[i] + '\n')