# Baekjoon Online Judge

# 20210126

# 7-1 (11654)
S = input()

print(ord(S))

# 7-2 (11720)
N = input()
N = int(N)

M = input()
M = list(map(int,M))

S = sum(M)

print(int(S))

# 7-3 (10809)
S = input()
S = list(S)

A = 'abcdefghijklmnopqrstuvwxyz'
A = list(A)

for i in (A):
    
    if (S.count(i) == 0):
        print('-1', end=' ')
    else: print(S.index(i), end=' ')
    
# 7-4 (2675)
N = input()
N = int(N)    

for i in range(N):
    
    R, S = input().split()
    R = int(R)
    S = list(S)
    
    for j in (S):
    
        print((j)*R, end='')
    
    print('')

# 7-5 (1157)
D = input().upper()
D = list(D)

U = set(D)
U = list(U)

num = 0
K = ''
for i in U:
    
    if (D.count(i) > num):
        num = D.count(i)
        K = i
    elif (D.count(i) == num):
        num = num
        K = '?'
    else:
        num = num
        K = K

print(K)
    