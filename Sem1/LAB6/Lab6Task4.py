import time
t_start = time.perf_counter()

def get(set, key):
    if key in set:
        return set[key][0]
    return '<none>'

def prev(set, key):
    if key in set.keys():
        if set[key][1] != None:
            local_key = set[key][1]
            return set[local_key][0]
    return '<none>'

def next(set, key):
    if key in set.keys():
        if set[key][2] != None:
            local_key = set[key][2]
            return set[local_key][0]
    return '<none>'

def put(set, key, value):
    global current_prev
    if key in set.keys():
        set[key][0] = value
        return
    set[key] = [value, None, None]
    set[key][1] = current_prev
    if current_prev != None:
        local_key = set[key][1]
        set[local_key][2] = key
    current_prev = key
    return

def delete(set, key):
    global current_prev
    if key in set.keys():
        if set[key][0] is not None and set[key][1] is not None and set[key][2] is not None:
            newnext = set[key][2]
            newprev = set[key][1]
            set[newprev][2] = newnext
            set[newnext][1] = newprev
        elif set[key][1] is None and set[key][2] is not None:
            local_key = set[key][2]
            set[local_key][1] = None
        elif set[key][2] is None and set[key][1] is not None:
            local_key = set[key][1]
            current_prev = local_key
            set[local_key][2] = None
        else:
            current_prev = None
        del set[key]
    return

set = {}
ans = []
current_prev = None

with open("input.txt", "r") as f:
    num_actions = int(f.readline())
    for i in range(num_actions):
        file = f.readline().strip().split(' ')
        if len(file) > 2:
            key, value = file[1], file[2]
            put(set, key, value)
        else:
            if file[0] == 'delete':
                key = file[1]
                delete(set, key)
            elif file[0] == 'get':
                key = file[1]
                ans.append(get(set, key))
            elif file[0] == 'prev':
                key = file[1]
                ans.append(prev(set, key))
            elif file[0] == 'next':
                key = file[1]
                ans.append(next(set, key))

with open("output.txt", "w") as d:
    for answer in ans:
        d.write(answer + '\n')


print("Время работы: %s секунд " % (time.perf_counter() - t_start))