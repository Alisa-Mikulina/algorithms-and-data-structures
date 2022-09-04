MAX_SIZE = 2 * 10 ** 6
MULT = 1019
PRIMARY = 10 ** 9 + 7


deg = [1 % PRIMARY]
find_ln = MAX_SIZE
for i in range(1, find_ln):
    deg.append((1019 * deg[i - 1]) % PRIMARY)


def hash(line):
    ln_line = len(line)
    hashed_pefixes = [0 for i in range(ln_line + 1)]
    hashed_pefixes[0] = 0
    for i in range(1, ln_line + 1):
        hashed_pefixes[i] = (hashed_pefixes[i - 1] + ord(line[i - 1]) * deg[i]) % PRIMARY
    return hashed_pefixes


def whether_equal(first, second, ln, full_ln, hashed):
    first_hashed = ((hashed[first + ln] - hashed[first]) * deg[full_ln - first]) % PRIMARY
    second_hashed = ((hashed[second + ln] - hashed[second]) * deg[full_ln - second]) % PRIMARY
    if first_hashed == second_hashed:
        return 'YES'
    return 'NO'


with open('input_4.txt') as f:
    line = f.readline().strip()
    hashed = hash(line)
    num_checks = int(f.readline())
    for line in f.readlines():
        first, second, ln = list(map(int, line.split()))
        print(whether_equal(first, second, ln, len(line), hashed))