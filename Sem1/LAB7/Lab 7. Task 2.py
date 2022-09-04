import time
t_start = time.perf_counter()


def calculator(number):
    pairs = dict()
    to_check = []
    to_check.append([number, None])
    while True:
        unwrap = to_check.pop(0)
        now, successor = unwrap[0], unwrap[1]
        if now not in pairs:
            pairs[now] = successor
            if now == 1:
                break
            if now % 3 == 0:
                to_check.append([now // 3, now])
            if now % 2 == 0:
                to_check.append([now // 2, now])
            to_check.append([now - 1, now])
    route = []
    key = 1
    while key:
        route.append(key)
        key = pairs[key]
    return len(route) - 1, route




with open("input_2.txt", "r") as f:
    number = f.readline()
    number = int(number)

ans = calculator(number)
for line in ans:
    print(line)


print("Время работы: %s секунд " % (time.perf_counter() - t_start))