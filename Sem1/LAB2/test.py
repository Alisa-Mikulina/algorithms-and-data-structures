with open("input.txt", "w") as f:
    ans = []
    for i in range(1000, 1, -1):
        ans.append(i)
    f.write(' '.join(list(map(str,ans))))