def count(s):
    global pairs
    global counter
    ans = 0
    for i in range (len(s)-1, -1, -1):
        if s[i] in pairs:
            for next in pairs[s[i]]:
                if next in counter:
                    ans += counter[next]

        if s[i] not in counter:
            counter[s[i]] = 0
        counter[s[i]] += 1
    print(ans)
   
with open('4.txt') as inp:
    lines = inp.readlines()
#inp = open('input.txt')
pairs = {}
counter = {}
n, k = map(int, lines[0].split())
s = lines[1]
for j in range(k):
    pair = lines[2+j]
    if pair[0] not in pairs:
        pairs[pair[0]] = []
    pairs[pair[0]].append(pair[1])
count(s)