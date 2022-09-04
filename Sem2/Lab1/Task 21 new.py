def win(num_my, num_beat, my_cards, to_beat, kos):
    if num_my < num_beat: 
        return 'NO'
    elif num_my == 0:
        return 'NO'
    elif len(my_cards[kos]) < len(to_beat[kos]):
        return 'NO'
    elif (len(my_cards[kos]) == 0) and (len(to_beat[kos]) != 0):
        return 'NO'
    while len(to_beat[kos]) != 0:
        cur_beat = to_beat[kos][0]
        beat = 0
        for i in range(len(my_cards[kos])):
            if my_cards[kos][i] > cur_beat:
                to_beat[kos].pop(0)
                my_cards[kos].pop(i)
                beat = 1
                break
        if beat == 0:
            return 'NO'
    types = ['S', 'C', 'D', 'H']
    for type in types:
        while len(to_beat[type]) != 0:
            cur_beat = to_beat[type][0]
            beat = 0
            if len(my_cards[type]) > 0:
                for i in range(len(my_cards[type])):
                    if my_cards[type][i] > cur_beat:
                        to_beat[type].pop(0)
                        my_cards[type].pop(i)
                        beat = 1
                        break
            if beat == 0:
                if len(my_cards[kos]) > 0:
                    for i in range(len(my_cards[kos])):
                        to_beat[type].pop(0)
                        my_cards[kos].pop(i)
                        beat = 1
                        break
            if beat == 0:
                return 'NO'
    beat_remain = 0
    for type in types:
        beat_remain += len(to_beat[type])
    if beat_remain == 0:
        return 'YES'
    else:
        return 'NO'





def reform(cards):
    equals = {'6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    reformed_cards = {'S': [], 'C': [], 'D': [], 'H': []}
    for i in range(len(cards)):
        reformed_cards[cards[i][1]].append(equals[cards[i][0]])
    for name, values in reformed_cards.items():
        sorted_values = sorted(values)
        reformed_cards[name] = sorted_values
    print(reformed_cards)
    return reformed_cards




with open('input.txt') as f:
    num_my, num_beat, kos =  list(f.readline().split())
    my_cards  = list(f.readline().split())
    to_beat  = list(f.readline().split())
    my_cards = reform(my_cards)
    to_beat = reform(to_beat)

ans = win(num_my, num_beat, my_cards, to_beat, kos)

with open('output.txt', 'w') as d:
    d.write(ans)