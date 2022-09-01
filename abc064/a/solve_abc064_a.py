s = input()
t = s.replace(' ', '')
# print(t)
u = int(t) % 4
if u == 0:
    print('YES')
else:
    print('NO')
    