def hash(line, primary):
    global deg
    num = 0
    for i in range(len(line)):
        letter = ord(line[i])
        num += letter * deg[len(line) - i - 1]
        num = num % primary
    hashed = num % primary
    return hashed


def precompute_hashes(find_ln, line, mult, primary):
    global deg
    hash_dict = {}
    hashes = [0 for i in range(len(line) - find_ln + 1)]
    first = line[:find_ln]
    hashes[0] = hash(first, primary)
    hash_dict[hashes[0]] = 0
    for i in range(len(hashes) - 1):
        old_hash = hashes[i]
        old_symb = ord(line[i])
        b_degreed = deg[find_ln - 1]
        new_symb = ord(line[i + find_ln])
        all_old = ((old_hash - old_symb * b_degreed) * mult) % primary
        new_hash = all_old + new_symb
        hashes[i + 1] = new_hash
        if new_hash in hash_dict.keys():
            continue
        else:
            hash_dict[new_hash] = i + 1
    return hash_dict


def binary_search(smaller, bigger, old_dividor, very_old_dividor, border, direction):
    global CURRENT_BIGGEST
    if old_dividor == very_old_dividor:
        return
    if direction == 'right':
        if (very_old_dividor + old_dividor) % 2 != 0:
            new_splitline = (very_old_dividor + old_dividor) // 2 + 1
        else:
            new_splitline = (very_old_dividor + old_dividor) // 2
    else:
        if (very_old_dividor - (very_old_dividor - old_dividor)) % 2 != 0:
            new_splitline = (very_old_dividor - (very_old_dividor - old_dividor)) // 2 + 1
        else:
            new_splitline = (very_old_dividor - (very_old_dividor - old_dividor)) // 2

    if new_splitline == 0 or new_splitline == border:
        return
    all_smol = precompute_hashes(new_splitline, smaller, mult, primary)
    all_big = precompute_hashes(new_splitline, bigger, mult, primary)
    found = (find_same(all_smol, all_big))
    if found[0] == True:
        CURRENT_BIGGEST = [found[1], found[2], new_splitline]
        direction = 'right'
    else:
        direction = 'left'
    binary_search(smaller, bigger, new_splitline, old_dividor, border, direction)



def find_same(all_smol, all_big):
    for key in all_smol.keys():
        if key in all_big.keys():
            id_1, id_2 = all_smol[key], all_big[key]
            return [True, id_1, id_2]
    return [False]


def find_biggest_subline(first, second):
    global mult, primary, CURRENT_BIGGEST
    if len(first) < len(second):
        smaller, bigger = first, second
    else:
        smaller, bigger = second, first
    tiny_len = len(smaller)
    if tiny_len % 2 != 0:
        first_splitter = tiny_len // 2 + 1
    else:
        first_splitter = tiny_len // 2
    all_smol = precompute_hashes(first_splitter, smaller, mult, primary)
    all_big = precompute_hashes(first_splitter, bigger, mult, primary)
    first_found = (find_same(all_smol, all_big))
    if first_found[0] == True:
        CURRENT_BIGGEST = [first_found[1], first_found[2], first_splitter]
        direction = 'right'
    else:
        direction = 'left'
    binary_search(smaller, bigger, first_splitter, tiny_len, tiny_len, direction)
    return




mult = 1019
primary = 10 ** 9 + 7

with open('input_7.txt') as f:
    for line in f.readlines():
        CURRENT_BIGGEST = [0, 0, 0]
        first, second = line.split()
        len_one, len_two = len(first), len(second)
        find_ln = max(len_one, len_two)
        deg = [1 % primary]
        for i in range(1, find_ln):
            deg.append((1019 * deg[i - 1]) % primary)
        find_biggest_subline(first, second)
        print(CURRENT_BIGGEST)