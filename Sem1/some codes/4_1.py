fin=open('input.txt','r',encoding='utf-8')
fout=open('output.txt','w',encoding='utf-8')
n = int(fin.readline())
arr = {}
current_prev = None
for i in range(n):
    command = fin.readline()
    command = command[0:-1]
    if command[0:2] == "ge":
        x = command[4:]
        fout.write(arr[x][0] if x in arr.keys() else "<none>")
        fout.write('\n')
    elif command[0:2] == "pr":
        x = command[5:]
        fout.write(arr[arr[x][1]][0] if x in arr.keys() and arr[x][1] is not None else "<none>")
        fout.write('\n')
    elif command[0:2] == "ne":
        x = command[5:]
        fout.write(arr[arr[x][2]][0] if x in arr.keys() and arr[x][2] is not None else "<none>")
        fout.write('\n')
    elif command[0:2] == "pu":
        x, y = command[4:].split()
        if x in arr.keys():
            arr[x][0] = y
        else:
            arr[x] = [y, None, None]
            arr[x][1] = current_prev
            if current_prev is not None:
                arr[arr[x][1]][2] = x
            current_prev = x
    else:
        x = command[7:]
        if x in arr.keys():
            if arr[x][0] is not None and arr[x][1] is not None and arr[x][2] is not None:
                newnext = arr[x][2]
                newprev = arr[x][1]
                arr[newprev][2] = newnext
                arr[newnext][1] = newprev
            elif arr[x][1] is None and arr[x][2] is not None:
                arr[arr[x][2]][1] = None
            elif arr[x][2] is None and arr[x][1] is not None:
                current_prev = arr[x][1]
                arr[arr[x][1]][2] = None
            else:
                current_prev = None
            del arr[x]
fin.close()
fout.close()