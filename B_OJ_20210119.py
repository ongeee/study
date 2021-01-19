# Baekjoon Online Judge


# 20210119

# 3-1 (2739)
N = input()
N = int(N)

for i in range(9):
    
    print(N, '*', int(i+1), '=', int(N*(i+1)))
    

# 3-2 (10950)
N = input()
N = int(N)    

A = []
B = []

for i in range(N):
    
    a, b = input().split()
    
    a = int(a)
    b = int(b)
    
    A.append(a)
    B.append(b)
    
for i in range(N):
    
    print(int(A[i]+B[i]))

# 3-3 (8393)
N = input()
N = int(N)

sum = 0
for i in range(N):
    
    sum = sum + (i+1)
    
print(sum)

# 3-4 (15552) [RE]
import sys

N = input()
N = int(N)

for i in range(N):
    
    A, B = sys.stdin.readline().split()
    
    A = int(A)
    B = int(B)

    print(int(A+B))

# 3-5 (2741)
N = input()
N = int(N)

for i in range(N):
    
    print(i+1)

# 3-6 (2742)
N = input()
N = int(N)

for i in range(N):
    
    print(N-i)
    
