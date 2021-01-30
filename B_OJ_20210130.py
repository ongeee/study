# Baekjoon Online Judge

# 20210130

# 8-1 (1712) [RE]
A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if (B >= C):
    print('-1')
    
else: 
    print(int(A // (C-B))+1)
    
# 8-2 (2292) [RE]
N = input()

N = int(N)
        
num = 1
six = 6
K = 1
if (N==1):
    print(num)

else:
    while True:
        
        K = K + six
        
        if (N<=K):
            num = num + 1 
            print(num)
            
            break
            
        else:
            num = num + 1
            six = six + 6        

# 8-3 (1193)

# 8-4 (2869) [RE]
A, B, V = input().split()

A = int(A)
B = int(B)
V = int(V)

if ((V-B) % (A-B) != 0):
    print(((V-B) // (A-B))+1)
    
else:
    print(((V-B) // (A-B)))

# 8-5 (10250) [RE]
N = input()

N = int(N)

for i in range(N):
    
    H, W, N = input().split()
    
    H = int(H)
    W = int(W)
    N = int(N)
    
    K = N % H
    
    if K ==0:
        floor = H
        num = (N // H)
    
    else:
        floor = K
        num = (N // H) + 1
        
    
    if (num<10):
        num = '0' + str(num)
        
    floor = str(floor)
    num = str(num)
    
    print(floor + num)

# 8-6 (2775)

# 8-7 (2839)

# 8-8 (10757)
A, B = input().split()

A = int(A)
B = int(B)

print(A+B)

# 8-9 (1011) 
     
        
    