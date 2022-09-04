import time
t_start = time.perf_counter()


def change(money, coins):
    min_num_coins = []
    for p in range(0, money + 1):
        min_num_coins.append(0)
    for m in range(1, money + 1):
        min_num_coins[m] = 10 ** 9
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coins[m - coins[i]] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]

with open("input_1.txt", "r") as f:
    money, k = f.readline().split(' ')
    money = int(money)
    coins = f.readline().split(' ')
    for i in range(len(coins)):
        coins[i] = int(coins[i])

ans = change(money, coins)
print(ans)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))