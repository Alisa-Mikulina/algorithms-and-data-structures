import time
t_start = time.perf_counter()

def make_palindrome(line):
    unique = {}
    odd = []
    palindrome = ""
    for letter in line:
        if letter not in unique:
            unique.setdefault(letter, 1)
        else:
            unique[letter] += 1
    unique_sorted = {i: unique[i] for i in sorted(unique)}

    for letter, amount in unique_sorted.items():
        if amount % 2 != 0:
            odd.append(letter)

    for letter in odd:
        unique_sorted[letter] -= 1

    unique_sorted_reversed = {i: unique_sorted[i] for i in sorted(unique_sorted, reverse=True)}

    for letter, amount in unique_sorted.items():
        palindrome += letter * (amount // 2)

    if odd != []:
        palindrome += odd[0]

    for letter, amount in unique_sorted_reversed.items():
        palindrome += letter * (amount // 2)

    return palindrome

f = open("input.txt", "r")
length = int(f.readline())
line = f.readline()
f.close()

d = open("output.txt", "w")
d.write(make_palindrome(line))
d.close()

print("Время работы: %s секунд " % (time.perf_counter() - t_start))