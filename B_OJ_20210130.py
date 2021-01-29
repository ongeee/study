# Baekjoon Online Judge

# 20210130

# 8-1 (1712) [RE]
    
# 8-2 (2292)
N = input()
    
N = int(N)

# 8-3 (1193)
N = input()
    
N = int(N)

# 8-4 (2869) [RE]

# 8-5 (10250) [RE]

# 8-6 (2775)
N = input()

N = int(N)

A, B = input().split()

A = int(A)
B = int(B)

# 8-7 (2839) [RE]
N = input()
N = int(N)

V = []

five_1 = N // 5
three_1 = (N % 5) // 3
Five_three_1 = five_1 + three_1

if ((N % 5) % 3 == 0):
    V.append(Five_three_1)

three_2 = N // 3
five_2 = (N % 3) // 5
Three_five_1 = five_2 + three_2 

if ((N % 3) % 5 == 0):
    V.append(Three_five_1)

eight_3 = N // 8

five_3_1 = (N % 8) // 5
three_3_1 = ((N % 8) % 5) // 3 
Five_three_2 = five_3_1 + three_3_1 + 2

if (((N % 8) % 5) % 3  == 0):
    V.append(Five_three_2)

three_3_2 = (N % 8) // 3
five_3_2 = ((N % 8) % 3) // 5
Three_five_2 = five_3_2 + three_3_2 + 2

if (((N % 8) % 3) % 5  == 0):
    V.append(Three_five_2)

if (len(V) == 0):
    print('-1')
else :
    print(min(V))

# 8-8 (10757)

# 8-9 (1011) 