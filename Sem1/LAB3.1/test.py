line = "First I rummaged my mind for words that could describe my personal nightmares"
i = len(line)
current_letter = ''
while i > -1:
    if line[i] == ' ':
        line = line + ' '
        i += 1
    else:
        start = i
        end = i
        while line[end] != ' ':
            current_letter = line[end]
            end += 1
        iteration = 0
        for j in range(start, end):
            line = line + line[j + iteration]
            iteration += 1
        i = end + 1



print(line)