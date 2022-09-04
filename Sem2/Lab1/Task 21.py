def win(num_my, num_beat, my_cards, to_beat, kos):
    if num_my < num_beat:
        return f'NO'
    elif to_beat[kos] != [] and my_cards[kos] == []:
        return f'NO'
    elif len(to_beat[kos]) > len(my_cards[kos]):
        return f'NO'
    types = ['S', 'C', 'D', 'H']
    if len(to_beat[kos]) != 0:
        while len(to_beat[kos]) != 0:
            cur_beat = to_beat[kos][-1]
            cur_mine = my_cards[kos][-1]
            if cur_mine > cur_beat:
                to_beat[kos].pop()
                my_cards[kos].pop()
            else:
                return f'NO'
    for type in types:
        if len(to_beat[type]) != 0:
            while len(to_beat[type]) != 0:
                cur_beat = to_beat[type][-1]
                if len(my_cards[type]) == 0:
                    if len(my_cards[kos]) == 0:
                        return f'NO'
                    my_cards[kos].pop(0)
                    to_beat[type].pop()

                    continue
                cur_mine = my_cards[type][-1]
                if cur_mine > cur_beat:
                    to_beat[type].pop()
                    my_cards[type].pop()

                    continue
                else:
                    if len(my_cards[kos]) == 0:
                        return f'NO'
                    my_cards[kos].pop(0)
                    to_beat[type].pop()
    return f'YES'


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

ans = win(int(num_my), int(num_beat), my_cards, to_beat, kos)

with open('output.txt', 'w') as d:
    d.write(ans)