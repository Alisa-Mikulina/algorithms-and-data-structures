def win(num_my, num_beat, my_cards, to_beat, kos):
    if num_my < num_beat: 
        return 'NO'
    elif num_my == 0:
        return 'NO'
    elif len(my_cards) < len(to_beat):
        return 'NO'
    elif (len(my_cards) == 0) and (len(to_beat) != 0):
        return 'NO'
    for cur_beat in to_beat:
        i = 0
        while True:
            if len(my_cards) == 0 or i >= len(my_cards):
                return 'NO'
            if my_cards[i][0] > cur_beat[0] and my_cards[i][1] == cur_beat[1]:
                my_cards.remove(my_cards[i])
                i += 1
                break
            elif my_cards[i][1] == kos and cur_beat[1] != kos:
                my_cards.remove(my_cards[i])
                i += 1
                break
            else:
                i += 1
    return 'YES'
            



def reform(cards, kos):
    equals = {'6': 1, '7': 2, '8': 3, '9': 4, 'T': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}
    reformed_cards = []
    for i in range(len(cards)):
        if cards[i][1] == kos:
            reformed_cards.append((equals[cards[i][0]] + 100, kos))
        else:
            reformed_cards.append((equals[cards[i][0]], cards[i][1]))
    sorted_values = sorted(reformed_cards)
    return sorted_values




with open('input.txt') as f:
    num_my, num_beat, kos =  list(f.readline().split())
    my_cards  = list(f.readline().split())
    to_beat  = list(f.readline().split())
    my_cards = reform(my_cards, kos)
    to_beat = reform(to_beat, kos)

print(my_cards)

ans = win(int(num_my), int(num_beat), my_cards, to_beat, kos)

with open('output.txt', 'w') as d:
    d.write(ans)