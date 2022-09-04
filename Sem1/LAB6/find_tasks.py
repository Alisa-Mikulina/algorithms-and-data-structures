A = 43
v = 8
p = 17

H = (A * v % p) % 9
print(H)

B = 1876

H = ((A * v + B) % p) % 9

print(H)