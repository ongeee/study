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

# 7-9 (2941)
S = input()
S = list(S)

# 7-10 (1316)
N = input()
N = int(N)

num = 0
for i in range(N):
    
    S = input()
    S = list(S)
    
    for j in range(len(S)):
        
        if (j==0):
            if (S[j]==S[j+1]):
                pass
            elif (S[j] in S[j+1:]):
                break
            
            
        elif (S[j]==S[j+1]) or (S[j]==S[j-1]):
            pass
        elif (S[j] in S[j+1:]):
            break
        
        num = num + 1
            
print(num)
    