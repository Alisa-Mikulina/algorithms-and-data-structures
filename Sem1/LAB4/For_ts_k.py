a = [192, 226, 242, 243, 240, 251]
c = 4993
d = 6649

for i in range(len(a)):
    print((a[i] ** d) % c)