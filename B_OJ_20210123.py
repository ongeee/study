# Baekjoon Online Judge

# 20210123

# 5-4 (3052)
K = []
for i in range(10):
    
    N = input()
    N = int(N)
    
    K.append(N%42)
    
K_len = len(list(set(K)))

print(int(K_len))

# 5-5 (1546)
N = input()
N = int(N)

score = map(int, input().split())
score = list(score)
    
sum = 0
for i in range(N):
    
    sum = sum + ((score[i]/max(score)) * 100)

avg = (sum/N)

print(avg)

# 5-6 (8958)
N = input()
N = int(N)

for i in range(N):

    A = input()
    A = list(A)
    
    sum = 0
    k = 0
    for j in (A[:]):
        
        if j == 'O':
            k = k+1
        else: k = 0
        
        sum = sum+k
        
    print(sum)
            
# 5-7 (4344)
N = input()
N = int(N)

for i in range(N):
    
    S = map(int, input().split())
    S = list(S)
    
    A = sum(S[1:]) / S[0]

    m = 0
    for j in (S[1:]):
        
        if j > A:
            m = m + 1
    
    P = m/S[0] *100
    
    print('%.3f%%' %(P))
