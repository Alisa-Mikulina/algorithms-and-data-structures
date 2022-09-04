line = "First I rummaged my mind for words that could describe my personal nightmares"
i = 0
current_letter = ''
while i < len(line):
    if line[i] == ' ':
        line = ' ' + line
        i += 2
    else:
        start = i
        end = i
        while line[end] != ' ':
            current_letter = line[end]
            end += 1
        iteration = 0
        for j in range(end, start - 1, -1):
            line = line[j + iteration] + line
            iteration += 1
        i = end + end + 1



print(line)