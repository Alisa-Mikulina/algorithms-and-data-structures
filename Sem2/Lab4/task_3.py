# import time
# t_start = time.perf_counter()


with open('input.txt') as f:
    to_find = f.readline().strip()
    text = f.readline().strip()
# print(len(text))

mult = 1019
primary = 10 ** 9 + 7
deg = [1 % primary]
find_ln = len(to_find)
for i in range(1, find_ln):
    deg.append((1019 * deg[i - 1]) % primary)



def hash(line, primary):
    num = 0
    for i in range(len(line)):
        letter = ord(line[i])
        num += letter * deg[len(line) - i - 1]
        num = num % primary
    hashed = num % primary
    return hashed


def precompute_hashes(find_ln, line, mult, primary):
    hashes = [0 for i in range(len(line) - find_ln + 1)]
    first = line[:find_ln]
    hashes[0] = hash(first, primary)
    for i in range(len(hashes) - 1):
        old_hash = hashes[i]
        old_symb = ord(line[i])
        b_degreed = deg[find_ln - 1]
        new_symb = ord(line[i + find_ln])
        all_old = ((old_hash - old_symb * b_degreed) * mult) % primary
        new_hash = all_old + new_symb
        hashes[i + 1] = new_hash
    return hashes


def RobinKarp(to_find, line):
    cnt = 0
    ans = []
    primary = 10 ** 9 + 7
    mult = 1019
    find_ln = len(to_find)
    hashed_find = hash(to_find, primary)
    hashed_all = precompute_hashes(find_ln, line, mult, primary)
    for i in range(len(hashed_all)):
        if hashed_all[i] != hashed_find:
            continue
        else:
            ans.append(str(i + 1))
            cnt += 1
    return (str(cnt), ' '.join(ans))



if len(to_find) > len(text):
    ans = 0
else:   
    ans = RobinKarp(to_find, text)

with open('output.txt', 'w') as d:
    if len(to_find) > len(text):
        d.write(str(ans))
    else:
        d.write(str(ans[0]) + '\n')
        d.write(ans[1])

# print("Время работы: %s секунд " % (time.perf_counter() - t_start))