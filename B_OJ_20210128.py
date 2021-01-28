# Baekjoon Online Judge

# 20210128

# 7-8 (5622) 
S = input()
S = list(S)

A = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for i in (S):
    
    for j in range(len(A)):
        
        if i in list(A[j]):
            time = time + 2 + (1+j)

print(time)

# 7-9 (2941) [RE]
S = input()

R = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in R:

    S = S.replace(i, 'r')

print(len(S))

####################  7-10 (1316) [RE]  ####################
cnt = 0

for _ in range(int(input())):
    
    x = input()
    cnt += 1
    for k in set(x):
        
        if len(set(x[x.index(k): x.rindex(k) + 1])) != 1:
            cnt -= 1
            break

print(cnt)
    