# Baekjoon Online Judge

# 20210120

# 3-7 (11021)
import sys

N = input()
N = int(N)

for i in range(N):
    
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    
    print('Case #%d: %d' %(int(i+1), int(A+B)))
          
# 3-8 (11022)
import sys

N = input()
N = int(N)

for i in range(N):
    
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    
    print('Case #%d: %d + %d = %d' %(int(i+1), A, B, int(A+B)))

# 3-9 (2438)
N = input()
N = int(N)

for i in range(N):
    
    # print('*' *(i))
    
    for s in range(i+1):
        
        print('*', end='')
        
    print('')

# 3-10 (2439)
N = input()
N = int(N)

for i in range(N):
    
    print(' ' *(N-(i+1)), end='')
    print('*' *(i+1))

# 3-11 (10871)
import sys
        
N, X = input().split()
N = int(N)
X = int(X)

K = sys.stdin.readline().split()
K = list(K)

for i in range(N):
    
    if (int(K[i])<X):
        print(int(K[i]), end=' ')
        
        
        