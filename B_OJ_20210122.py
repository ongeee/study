# Baekjoon Online Judge

# 20210122

# 5-1 (10818)
N = input()
N = int(N)

M = map(int, input().split())
M = list(M)
    
print(min(M), end=' ')
print(max(M))

# 5-2 (2562) [RE]
N = []
for i in range(9):
    
    K = input()
    K = int(K)
    
    N.append(K)
    
print(max(N))
print(int(N.index(max(N))+1))
    
# 5-3 (2577) [RE]
A = int(input())
B = int(input())
C = int(input())

mul = list(str(A*B*C))

for i in range(10):
    
    print(mul.count(str(i)))
