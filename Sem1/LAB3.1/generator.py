import random

a = [random.randint(1, 40000) for i in range(10 ** 6)]
b = [random.randint(1, 40000) for i in range(10 ** 6)]
with open("input.txt", "w") as d:
    d.write("1 1")
    d.write("\n")
    d.write(' '.join(list(map(str, a))))
    d.write("\n")
    d.write(' '.join(list(map(str, b))))

# a = [i for i in range((10 ** 4), -(10 ** 4), -1)]
# with open("input", "w") as d:
#     d.write("1")
#     d.write("\n")
#     d.write(' '.join(list(map(str, a))))