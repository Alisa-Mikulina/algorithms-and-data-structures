def find_subline(line, fin_len):
    stripped_line = list(line)
    len_line = len(line)
    pref = [0 for i in range(len_line)]
    j = 0

    for i in range(2, len_line + 1):
        while j > 0 and stripped_line[j] != stripped_line[i - 1]:
            j = pref[j - 1]
        if stripped_line[j] == stripped_line[i - 1]:
            j += 1
        pref[i - 1] = j
    ans = ''
    for i in range(len(pref)):
        if pref[i] == fin_len:
            ans += str(i - 2 * fin_len) + ' '
    return ans



with open('input.txt') as f:
    line = f.readline().strip()
    to_find = f.readline().strip()
    fin_len = len(to_find)
    zhaba = to_find + '#' + line # zhaba is a mix of the line we need to find and the line itself, separated by #
    ans = find_subline(zhaba, fin_len)

with open('output.txt', 'w') as d:
    d.write(ans.strip())