# Baekjoon Online Judge

# 20210127

# 7-6 (1152) [RE]
S = input().split()
S = list(S)

print(len(S))

# 7-7 (2908) [RE]
A, B = input().split()
A = list(A)
B = list(B)

A.reverse()
B.reverse()

A = int("".join(A))
B = int("".join(B))

if (A>B): print(A)
else: print(B)
