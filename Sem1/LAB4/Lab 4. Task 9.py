import time
t_start = time.perf_counter()

# в процессе переписывания поняла, что тут хвост не нужен, не дает ничего, ведь можно просто аппендить и все
# более того, тут не нужны расчеты, поэтому в хвосте вообще потерялся смысл
# как-то так это выглядит теперь, если есть какие-то вопросы, или еще что нужно подправить, можно в лс в тг: @mikalicce
# p.s. всей душой советую почитать крик души в отчете, там есть шуточки :)

def add(queue_1, queue_2, number):
    global nose_1, nose_2
    queue_2.append(number)
    if len(queue_1) - nose_1 + 1 <= len(queue_2) - nose_2:
        queue_1.append(queue_2[nose_2])
        nose_2 += 1

def naglo_add(queue_1, queue_2, number):
    global nose_1, nose_2
    queue_1.append(number)
    if len(queue_1) - nose_1 + 1 < len(queue_2) - nose_2:
        queue_1.append(queue_2[nose_2])
        nose_2 += 1

def delete(queue_1, queue_2):
    global nose_1, nose_2
    if queue_1 == []:
        answer = queue_2[0]
        nose_2 += 1
    else:
        answer = queue_1[nose_1]
        nose_1 += 1
    if len(queue_1) - nose_1 < len(queue_2) - nose_2:
        queue_1.append(queue_2[nose_2])
        nose_2 += 1
    return answer


queue_1 = []
queue_2 = []
ans = []
nose_1, nose_2 = 0, 0

with open("input.txt", "r") as f:
    iterations = int(f.readline())
    for i in range(iterations):
        line = f.readline().strip()
        if len(line) > 2:
            action, number = list(line.split(" "))
            if action == '+':
                add(queue_1, queue_2, number)
            else:
                naglo_add(queue_1, queue_2, number)
        else:
            action = line
            ans.append(delete(queue_1, queue_2))


with open("output.txt", "w") as d:
    for elem in ans:
        d.write(str(elem) + '\n')

print("Время работы: %s секунд " % (time.perf_counter() - t_start))