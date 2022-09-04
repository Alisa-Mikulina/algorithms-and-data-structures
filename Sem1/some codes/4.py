fin = open("input.txt")
fout = open("output.txt", 'w')
n = int(fin.readline())
pam = dict()
tail = None
for _ in range(n):
    command = fin.readline().split()
    if command[0] == "put":
        if command[1] in pam:
            pam[command[1]][1] = command[2]
        else:
            if tail is not None:
                pam[tail][2] = command[1]
            pam.update({command[1]: [tail, command[2], None]})
            tail = command[1]

    elif command[0] == "delete":
        if command[1] in pam:
            if pam[command[1]][0] is None and pam[command[1]][2] is None:
                tail = None
            elif pam[command[1]][0] is None:
                pam[pam[command[1]][2]][0] = None
            elif pam[command[1]][2] is None:
                pam[pam[command[1]][0]][2] = None
                tail = pam[command[1]][0]
            else:
                pam[pam[command[1]][2]][0] = pam[command[1]][0]
                pam[pam[command[1]][0]][2] = pam[command[1]][2]
            del pam[command[1]]
            
    elif command[0] == "get":
        if command[1] in pam:
            print(pam[command[1]][1], file=fout)
        else:
            print("<none>", file=fout)
    elif command[0] == "prev":
        if command[1] in pam:
            if pam[command[1]][0] is not None:
                print(pam[pam[command[1]][0]][1], file=fout)
            else:
                print("<none>", file=fout)
        else:
            print("<none>", file=fout)        
                
    elif command[0] == "next":
        if command[1] in pam:
            if pam[command[1]][2] is not None:
                print(pam[pam[command[1]][2]][1], file=fout)
            else:
                print("<none>", file=fout)
        else:
            print("<none>", file=fout)

fin.close()
fout.close()