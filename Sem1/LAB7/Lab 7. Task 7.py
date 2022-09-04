import time
t_start = time.perf_counter()


def is_samplified(sample, word):
    max_length = len(word)
    insert_at = None
    i = 0
    while i != max_length:
        if i >= len(sample):
            return 'YES'
        if sample[i] == word[i]:
            i += 1
            continue
        if sample[i] != '*' and sample[i] != '?' and sample[i] != word[i]:
            if sample[i - 1] == '*':
                sample = sample[:i] + '*' + sample[i:]
                i += 1
                continue
            elif i == insert_at:
                sample = sample[:i] + '*' + sample[i:]
                i += 1
                continue
            else:
                return 'NO'
        if sample[i] == '?':
            if i + 1 < len(sample) - 1:
                i += 1
                continue
            else:
                return 'NO'
        if sample[i] == '*':
            if i == len(sample) - 1:
                return 'YES'
            insert_at = i
            sample = sample[:i] + sample[i + 1:]

    return 'YES'




with open('input_7.txt', 'r') as f:
    sample = f.readline().strip()
    word = f.readline()

print(sample, word)
ans = is_samplified(sample, word)
print(ans)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))