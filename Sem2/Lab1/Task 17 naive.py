def count_phone_numbers(length, abilities, steps, iter, elems):
    if length == 1:
        return 8
    if iter == length:
        count = 0
        for elem in elems:
            count += abilities[elem]
    if iter == 1:
        count = 8
        for i in elems:
            count += count_phone_numbers(length, abilities, steps, iter + 1, elems=steps[i])
        return count
    local_count = 0
    for elem in elems:
        local_count += abilities[elem]
        local_count += count_phone_numbers(length, abilities, steps, iter + 1, steps[elem])
    return local_count

    



field = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9], 
         ['.', 0, '.']
         ]
abilities = {1: 2, 2: 2, 3: 2, 4: 3, 5: 0, 6: 3, 7: 2, 8: 2, 9: 2, 0: 2}
steps = {1: [6, 8], 2: [7, 9], 3: [8, 4], 4: [9, 3, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}
print(abilities)
length = int(input())
iter = 1
count = 0
ans = count_phone_numbers(length, abilities, steps, iter, [1, 2, 3, 4, 6, 7, 9])
print(ans)